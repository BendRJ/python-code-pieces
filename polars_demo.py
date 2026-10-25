# /// script
# requires-python = ">=3.14"
# dependencies = ["polars>=2.0"]
# ///

from pathlib import Path
import polars as pl

FILE = Path() / "data" / "netflix_titles.csv"

# read_ loads df into memory directly
full_df = pl.read_csv(FILE)
print(full_df.head())

# lazy dataframe with scan_csv or via pl.DataFrame.lazy() to only get a query plan
# lazy_df = dataframe.lazy()
lazy_df = pl.scan_csv(FILE) # nothing read yet, only the path + schema
print(f"This is the query plan: {lazy_df.explain()}")
print(f"This is the schema: {lazy_df.collect_schema()}")

# sql is first class citizen
query = "SELECT type, release_year, count(1) show_id_cnt from self where country = 'Germany' group by 1,2 order by release_year desc"
result = lazy_df.sql(query).collect() #.collect() to materialize lazy df, befre its only a query plan
print(result)

# same result can be obtained using chained methods
q = (
    pl.scan_csv(FILE)
    .filter(pl.col("country") == "Germany")
    #predicate pushdown: filters are applied while reading, rows dont match dont get loaded into memory
    .group_by(["type", "release_year"])
    .agg(pl.col("show_id").count())
    .sort("release_year", descending=True)
)
df = q.collect()
print(df)

# sink_csv streams the result of a lazy query straight to a file without building a DataFrame in memory first
OUTPUT_FILE = Path() / "data" / "germany_titles_by_year.csv"
q.sink_csv(OUTPUT_FILE)
print(f"Written to {OUTPUT_FILE}: {pl.read_csv(OUTPUT_FILE).head()}")

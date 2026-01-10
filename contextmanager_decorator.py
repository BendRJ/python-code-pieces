# @contextmanager is a built in python decorator that lets you create your own with blocks using a normal function instead of a complex class.
# “setup → do something → clean up safely”
# use case: file handling, database connections, or temporary changes in state (everywhere you need guaranteed cleanup)
# try except finally is the traditional way to ensure cleanup, but contextmanager removes boilerplate and makes code cleaner.
# combining contextmanagers and try except finnaly is also possible to handle user code exceptions while ensuring cleanup.

from contextlib import contextmanager

@contextmanager
def get_number():
    print("Setup")
    yield 42 # ← The 'with' block runs here ! what comes after yield is assigned to the variable after 'as' in the with statement
    print("Cleanup")

with get_number() as number:
    print(number)


# Example: Database connection context manager
class MockConnection:
    """Simulates a database connection"""
    
    def __init__(self, connection_id: int):
        self.connection_id = connection_id
        self.is_open = True
        self.transaction_active = False
        print(f"  🔌 [Connection {connection_id}] OPENED")
    
    def commit(self):
        """Commit the transaction"""
        if not self.is_open:
            raise RuntimeError("Connection is closed!")
        print(f"  ✅ [Connection {self.connection_id}] COMMITTED")
        self.transaction_active = False
    
    def rollback(self):
        """Rollback the transaction"""
        if not self.is_open:
            raise RuntimeError("Connection is closed!")
        print(f"  ↩️  [Connection {self.connection_id}] ROLLED BACK")
        self.transaction_active = False
    
    def close(self):
        """Close the connection"""
        if self.is_open:
            print(f"  🔒 [Connection {self.connection_id}] CLOSED")
            self.is_open = False
        else:
            print(f"  ⚠️  [Connection {self.connection_id}] Already closed!")
    
    def execute(self, sql: str):
        """Execute SQL (simulated)"""
        if not self.is_open:
            raise RuntimeError("Connection is closed!")
        self.transaction_active = True
        print(f"  📝 [Connection {self.connection_id}] Executing: {sql}")


@contextmanager
def safe_connection():
    conn = MockConnection(1)
    try:
        yield conn  # User code runs here
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

# Now users write clean code:
with safe_connection() as conn:
    conn.execute("SELECT 1")

# Again?
with safe_connection() as conn:
    conn.execute("INSERT INTO table VALUES (1)")

# 10 queries = 10 simple 'with' statements!

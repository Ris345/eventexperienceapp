import os
import shutil

# implemented a delete that would allow for clearing pycached and generated db file


def delete_files_folders(dir):
    items = os.listdir(dir)
    for item in items:
        item_path = os.path.join(dir, "__pycache__")
        if os.path.isdir(item_path):
            # delete __pyache__ dir
            shutil.rmtree(item_path)
            print(f"delete dir: {item_path}")


if __name__ == "__main__":
    base = "server"
    delete_files_folders(base)
    nested = ["queries", "routes"]
    for dir in nested:
        full_path = os.path.join(base, dir)
        delete_files_folders(full_path)

    db = "server_sql_app.db"
    db_path = os.path.join(base, db)
    if os.path.exists(db_path):
        os.remove(db_path)
        print("delete db")

print("done")

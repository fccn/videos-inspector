import os
import sys
import time
from app.services.inspect_video_service import InspectVideosService

if __name__ == "__main__":
    try:
        file_name = str(sys.argv[1])
        file_name = file_name.replace(".xlsx", "")
    except:
        sys.stdout.write("""
You must provide the parameter:
    - file name (str)
\n""")
        exit()

    sys.stdout.write(f"""
Starting to inspect...
The provided file name: {file_name}
The time to inspect increases according to the file size!
\n"""
    )

    output_dir = os.path.join(os.getcwd(), 'output')
    os.makedirs(output_dir, exist_ok=True)
    output_save_path = os.path.join(output_dir, f"{file_name}.xlsx")

    start = time.time()
    InspectVideosService().handle_steps_to_inspect_videos(f"{file_name}.xlsx", output_save_path)
    finish = time.time() - start
    sys.stdout.write(f"Inspection finished with {finish} seconds.\n")
    sys.stdout.write(f"Get the generated file in the output directory\n")
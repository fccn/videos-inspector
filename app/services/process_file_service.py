import os
from services.inspect_video_service import InspectVideosService

class ProcessFileService:

    @staticmethod
    def process_file(file):
        save_path = os.path.join(os.getcwd(), file.filename)
        file.save(save_path)

        output_dir = os.path.join(os.getcwd(), 'output')
        os.makedirs(output_dir, exist_ok=True)
        output_save_path = os.path.join(output_dir, file.filename)

        InspectVideosService().handle_steps_to_inspect_videos(file.filename, output_save_path)

        return output_save_path
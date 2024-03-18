@upload_jpgs_blueprint.route('/upload_jpgs', methods=['GET', 'POST'])
def upload_jpgs(test_names):
    files = request.files.getlist('jpg')
    total_files = len(files)
    uploaded_count = 0

    for jpg_file in files:
        if jpg_file.filename == '':
            return jsonify({'error': 'No selected file'})

        if jpg_file and allowed_marker(jpg_file.filename):
            filename = secure_filename(jpg_file.filename)
            file_path = os.path.join('jpgs', filename)
            
            try:
                with open(file_path, 'wb') as f:
                    f.write(jpg_file.stream.read())
            except Exception as e:
                # Log the error
                logging.error(f"Error saving file '{filename}': {e}")
                continue  # Continue with the next file
    return jsonify({'name' : test_names.filename,
                    'status' : 'success'})
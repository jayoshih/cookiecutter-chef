import zipfile
import os
import zipfile

class HTMLWriter():
    """
        Class for writing zipfiles
    """

    zf = None               # Zip file to write to
    write_to_path = None    # Where to write zip file

    def __init__(self, write_to_path):
        """ Args: write_to_path: (str) where to write zip file """
        self.map = {}                       # Keeps track of content to write to csv
        self.write_to_path = write_to_path  # Where to write zip file

    def __enter__(self):
        """ Called when opening context (e.g. with HTMLWriter() as writer: ) """
        self.open()
        return self

    def __exit__(self, type, value, traceback):
        """ Called when closing context """
        self.close()

    def _write_to_zipfile(self, filename, content):
        if filename not in self.zf.namelist():
            info = zipfile.ZipInfo(filename, date_time=(2013, 3, 14, 1, 59, 26))
            info.comment = "HTML FILE".encode()
            info.compress_type = zipfile.ZIP_STORED
            info.create_system = 0
            self.zf.writestr(info, content)

    """ USER-FACING METHODS """

    def open(self):
        """ open: Opens zipfile to write to
            Args: None
            Returns: None
        """
        self.zf = zipfile.ZipFile(self.write_to_path, "w")

    def close(self):
        """ close: Close zipfile when done
            Args: None
            Returns: None
        """
        self.zf.close()

    def write_file(self, filename, contents, directory="src"):
        """ write_file: Write files referenced by main file
            Args:
                filename: (str) name of file in zip
                contents: (str) contents of file
                directory: (str) directory in zipfile to write file to (optional)
            Returns: path to file in zip
        """
        filepath = "{}/{}".format(directory, filename)

        self._write_to_zipfile(filepath, contents)
        return filepath

    def write_main_file(self, contents):
        """ write_main_file: Write main index file to zip
            Args:
                contents: (str) contents of file
            Returns: path to file in zip
        """
        self._write_to_zipfile('index.html', contents)
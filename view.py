
from flask import Flask, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
import subprocess
from LAS_Processor import LAS_Processor


# TO-DO: limit the file type to LAS format
# TO-DO: limit the file size to 1.5 GB
UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'las'}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

class UploadFileForm(FlaskForm):
    file = FileField("File")
    submit = SubmitField("Submit")


# A boolean variable to mark if rendering/visualization script is running
rendering_in_progress = False

@app.context_processor
def handle_context():
    return dict(os=os)

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():

    global form 
    global filename
    global rendering_in_progress
    filename = ""
    
    # TO-DO: everytime we refresh the homepage, the static files folder should be cleared
    
    # if visualization script is running, terminate the process
    if rendering_in_progress:
        subprocess.Popen.kill(process)
        rendering_in_progress = False
        
    form = UploadFileForm()
    
    # when the "Submit" button is clicked, save the selected file in the static/files folder
    if form.validate_on_submit():
        
        # get the file data from frontend
        file = form.file.data
        
        # save the file name as a global variable, since we need to use it outside of this function
        filename = file.filename
        
        # save the file under static/files folder
        if (filename != ""):
            file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename(filename)))

    if filename == "":
        # if no file is selected, render the homepage without any message
        return render_template('/index.html', form=form)
    else:
        # send a notification to the terminal when the file is saved successfully
        message = filename + " is submitted"
        
        return render_template('/index.html', 
                               form=form, 
                               message_after_uploading = message,
                               filename = filename)


@app.route("/visualize/", methods=['POST'])
def visualize_data():
    
    global rendering_in_progress
    global filename

    message = ""
    
    if rendering_in_progress == True:
        message = "Cannot start a new rendering process. Please click the 'Stop Visualization' button"
    elif filename == "":
        message = "Please upload a file"
    else:
        
        message = "Visualization in progress"
        
        rendering_in_progress = True
        
        command = "python3 LAS_Processor.py " + filename
        global process 
        process = subprocess.Popen(command, shell=True)
        
        # Initailize a LAS_Processor object
        # TO-DO: this process takes time. How can we track it and show it in progress bar?
        file_path = './static/files/' + filename
        las_processor = LAS_Processor(file_path)
        las_processor.process() 
        
        # get the point statistics and return the point statistics to the frontend
        point_stats = las_processor.get_point_statistics()
        
        # number of points for natural features
        ground_num = point_stats[2]
        low_veg_num = point_stats[3]
        med_veg_num = point_stats[4]
        high_veg_num = point_stats[5]
        water_num = point_stats[9]
        
        # number of points classified as non-natural features
        non_natural_num = point_stats[6] + point_stats[10] + point_stats[11]
        + point_stats[13] + point_stats[14] + + point_stats[15] + point_stats[16] + point_stats[17]
        
        # total number of points
        total = 0
        for classification in point_stats:
            total += point_stats[classification]

        print("\nPoint calculation finished\n")
 
        # wait until the image is generated and saved
        while True:
           if os.path.isfile("static/img.png"):
               break
    
        return render_template('/index.html', 
                           form=form, 
                           visualization_start_message = message,
                           filename = filename,
                           ground_num = ground_num, 
                           low_veg_num = low_veg_num, 
                           med_veg_num = med_veg_num,
                           high_veg_num = high_veg_num,
                           water_num = water_num,
                           non_natural_num = non_natural_num,
                           ground_perc = "{:.1f}".format(ground_num / total * 100),
                           low_veg_perc = "{:.1f}".format(low_veg_num / total * 100),
                           med_veg_perc = "{:.1f}".format(med_veg_num / total * 100),
                           high_veg_perc = "{:.1f}".format(high_veg_num / total * 100),
                           water_perc = "{:.1f}".format(water_num / total * 100),
                           non_natural_perc = "{:.1f}".format(non_natural_num / total * 100))
    
    return render_template('/index.html', 
                            form=form, 
                            visualization_start_message= message,
                            filename = filename)


@app.route("/stop_visualization/", methods=['POST'])
def stop_visualization():
    global rendering_in_progress
    
    message = "No visualization process is running"
  
    if rendering_in_progress == True:
        subprocess.Popen.kill(process)
        message = "Visualization terminated"
        rendering_in_progress = False
    return render_template('/index.html', form=form, visualization_stop_message = message)


# This starts the flask app configured to listen on port 5500
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5500))
    app.run(debug=True, host='0.0.0.0', port=port)
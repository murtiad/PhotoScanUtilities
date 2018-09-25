# open Photoscan
import PhotoScan
# create the object to store project info
doc = PhotoScan.app.document
# open the project
doc.open('project_PS.psz')
# create the object to store chunk info
chunk = doc.chunk
# load the GPS and IMU file (CSV format)
chunk.loadReference('file_aerial_control.csv', PhotoScan.ReferenceFormatCSV , 'nxyzabc',  ',')
# save the project
# doc.save()

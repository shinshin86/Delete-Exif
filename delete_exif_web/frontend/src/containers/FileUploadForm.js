import React, { Component } from 'react'
import { PropTypes } from 'prop-types'
import { connect } from 'react-redux'
import Dropzone from 'react-dropzone'
import { deleteExif } from '../actions'
import { Button } from 'react-bootstrap'
import { circularLoading }  from '@yami_beta/react-circular-loading'

const styles = {
  loadingCircle: {
    position: "fixed",
    top: 100,
    left: 300
  }
}
const CircularLoading = circularLoading({
  num: 12,
  distance: 5,
  dotSize: 2,
  speed: 1200,
});

class FileUploadForm extends Component {
  constructor(props, context) {
    super(props, context);

    this.state = {
      acceptedFiles: [],
      rejectedFiles: [],
    };
  }

  handleDrop(accepted, rejected) {
    this.setState({ acceptedFiles: accepted, rejectedFiles: rejected })
  }

  handleChangeFile(e) {
    const target = e.target;
    const file = target.files.item(0);
    this.updateFile(new Array(file));
  }
  updateFile(f) {
    this.setState({ acceptedFiles: f })
  }
  processingResult(data) {
    if(data.result) {
      let filenames = ''
      data.map(file => {
        filenames += file.name
        filenames += ','
      })
      return `Delete Exif File : ${filenames}`
    } else if (data.result === false) {
      return `Failure Delete Exif`
    } else {
      return `Select Delete Exif File...`
    }
  }

  render() {
    const { data, deleteExif, isProcessing }  = this.props
    console.log(data)
    return (
      <div>
        <div>
          <h3>{this.processingResult(data)}</h3>
          { isProcessing && <CircularLoading style={styles.loadingCircle} /> }
          <Dropzone
            ref={(node) => this.dropzone = node}
            accept="image/jpeg,image/jpg"
            onDrop={(accepted, rejected)=> this.handleDrop(accepted, rejected)}
          >
            Delete Exif File is Here...
          </Dropzone>
          <input type="file" onChange={(e) => this.handleChangeFile(e)}/>

          <div className="uploadFile">
            <div>Accepted files</div>
            <ul>
              {this.state.acceptedFiles.map(f => <li key={f.name}>File name : {f.name}<br />File size : {f.size}</li>)}
            </ul>
            <div>Rejected files</div>
            <ul>
              {this.state.rejectedFiles.map(f => <li key={f.name}>File name : {f.name}<br />File size : {f.size}</li>)}
            </ul>
          </div>

          <Button bsStyle="primary" onClick={() => deleteExif(this.state.acceptedFiles)}>
            Upload
          </Button>
        </div>
      </div>
    )
  }
}

function mapStateToProps(state) {
  const { exif } = state
  const { isProcessing, data } = exif || {
    isProcessing: false,
    data: {}
  }

  return {
    isProcessing,
    data
  }
}

export default connect(mapStateToProps, { deleteExif } )(FileUploadForm)

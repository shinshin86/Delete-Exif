import React, { Component } from 'react'
import { PropTypes } from 'prop-types'
import { connect } from 'react-redux'
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
      file: []
    };
  }

  handleChangeFile(e) {
    const target = e.target;
    const file = target.files.item(0);
    this.updateFile(file);
  }
  updateFile(f) {
    this.setState({ file: f })
  }

  render() {
    const { data, deleteExif, isProcessing }  = this.props
    return (
      <div>
        <div>
          Delete Exif File : {data.name}<br />
          { isProcessing && <CircularLoading style={styles.loadingCircle} /> }
          <input type="file" onChange={(e) => this.handleChangeFile(e)}/>
          <Button bsStyle="primary" onClick={() => deleteExif(this.state.file)}>
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

import { take, put, call, fork } from 'redux-saga/effects'
import{
  DELETE_EXIF, successDeleteExif, failureDeleteExif
} from '../actions'
import fetch from 'isomorphic-fetch'
import FileSaver from 'file-saver';

export function* handleDeleteExif() {
  while(true) {
    const action = yield take(DELETE_EXIF)
    const data = yield call(fileUpload, action.file)

    if(data) {
      yield put(successDeleteExif(action.file))
    } else {
      yield put(failureDeleteExif())
    }
  }
}

function fileUpload(file){
  const url = 'http://localhost:3001/upload'

  const formData = new FormData()
  formData.append('upload_file', file)

  return fetch(url, {
    method: 'POST',
    body: formData
  })
    .then(res => {
      if (res.status === 200) {
        return res.blob()
      } else {
        console.error("ERROR: Not response status 200")
      }
    })
    .then(blob => {
      FileSaver.saveAs(blob, file.name)
      return true
    })
    .catch(err => {
      console.error(`ERROR: ${err}`)
      throw new Error('ERROR')
    })
}

export default function* root() {
  yield fork(handleDeleteExif)
}

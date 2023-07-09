import axios from 'axios'
import {useToast} from "vue-toastification";

const toast = useToast()
class BaseApi {
    constructor(BASE_URL = "") {
        this.BASE_URL = BASE_URL
    }
    _request(params) {
        if (!params.method) params.method = 'get'
        params.baseURL = this.BASE_URL
        return new Promise((resolve, reject) => {
            axios(params)
                .then(res => resolve(res.data))
                .catch(err => {
                    let errMessage = null
                    if (err.response) {
                        if (err.response.data.detail) {
                            errMessage = err.response.data.detail
                        }
                    }
                    if (!errMessage) {
                        errMessage = err.toString()
                    }
                    toast.error(errMessage)
                    reject(err)
                })
        })
    }
    getSupportRequests(params){
        return this._request({
            url: `/support_request`,
            params: params
        })
    }
    getSupportRequestFields(){
        return this._request({
            url: `/support_request/fields`,
        })
    }
}

const api = new BaseApi('/api')

export { api }

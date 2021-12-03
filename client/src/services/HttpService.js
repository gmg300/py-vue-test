import http from '@/util/http'
import env from '@/environment'

class HttpService {
    constructor(){
        this.http = http;
        this.base_url = env.base_url
    }
}

export default HttpService
import axios from 'axios';
import env from '@/environment.js'

class Http {
    constructor(params = {}) {
        this.base_url = params.base_url;
        this.http = axios.create({
            headers: {
                'Content-Type': 'application/json'
            },
            withCredentials: true
        })
    }
    async request(method, url_path, params = {}, config = {}) {
        const url = `${this.base_url}${url_path}`
        const response = await this.http[method](url, params, {
            ...config
        });
        return response;
    }
    async get(url_path = '', params = {}, config = {}) {
        return await this.request("get", url_path, params, config);
    }
    async put(url_path = '', params = {}, config = {}) {
        return await this.request("put", url_path, params, config);
    }
    async post(url_path = '', params = {}, config = {}) {
        return await this.request("post", url_path, params, config);
    }
    async delete(url_path = '', params = {}, config = {}) {
        return await this.request("delete", url_path, params, config);
    }
}


export default new Http({
    base_url: env.API_BASE_URL
});
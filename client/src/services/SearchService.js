import HttpService from '@/services/HttpService';

class SearchService extends HttpService {
    constructor(params = {}) {
        super();
        this.params = params;
    } 
    async get(type, value) {
        const url = `search/${type}/${value}`;
        const result = await this.http.get(url);
        console.debug("RESULT", result);
        return result;
    }
}

export default new SearchService();
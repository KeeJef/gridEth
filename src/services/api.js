import axios from 'axios';

export default {

    getSquares() {
        return axios.get('http://localhost:5000/squares').then(response => {
            return response.data
        })

    }
}


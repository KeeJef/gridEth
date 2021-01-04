import axios from 'axios';

export default {

    getSquares() {
        return axios.get('http://localhost:5000/squares').then(response => {
            return response.data
        })

    },

    async getSquaresAsync() {
        try{
          let response = await axios.get('http://localhost:5000/squares')
          return response.data
        }catch(err){
          console.log(err)
        }
      }
}


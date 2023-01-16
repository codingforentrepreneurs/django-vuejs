import {reactive} from 'vue'


export default store = reactive({
    token: null,
    setToken(newToken) {
        this.token = newToken
    },
    count: 0,
    increment (event) {
        if (event) {
            event.preventDefault();
        }
        this.count ++
    }
})
<script setup>
import axios from 'axios'
import { reactive, onMounted} from 'vue'
let data = reactive({
    title: 'Hello World',
    contentList: []
})
// let title = ref("Hello world")
// let contentList = ref([])

onMounted(async ()=>{
    let response;
    try {
        response = await axios.get('/api/posts/')
    } catch(error) {
        response = error.response
    }
    
    if (response.status === 200) {
        let responseData = response.data
        data.title  = "Post" 
        data.contentList = responseData.data
    } else {
        data.title = "Not Found"
    }


 
})





</script>

<template>
    <div>
        <h1>{{ data.title }}</h1>
        <div v-for="post of data.contentList" :key="post.id">
            {{ post.id }} - {{ post.title }}
        </div>
    </div>
</template>
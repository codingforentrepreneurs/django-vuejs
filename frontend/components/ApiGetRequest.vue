<script setup>
import { reactive, onMounted} from 'vue'
let data = reactive({
    title: 'Hello World',
    contentList: []
})
// let title = ref("Hello world")
// let contentList = ref([])

onMounted(async ()=>{
    let responseData = await fetch('/api/posts/').then(res=>{
        if (res.status === 200) {
            return res.json()
        } else {
            return "Not found"
        }
    })
    if (responseData instanceof String || typeof(responseData) === "string") {
        data.title = responseData
    } else {
        data.title  = "Post"
        data.contentList = responseData.data
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
<script setup>
import axios from 'axios'
import store from './../store'
import {reactive} from 'vue'
const formData = reactive({
    'title': '',
    'slug': '',
})
const handleAutoSlugChange = (event) =>{
    // console.log(formData.title)
    // console.log(event.target.value)
    // formData.slug = slugify(event.target.value)
    formData.slug = event.target.value
}

const handleSubmitForm = async (event) => {
    if (event) {
        event.preventDefault()
    }
    const target = event.target
    const innerFormData = new FormData(target)
    const innerFormDataJson = JSON.stringify(Object.fromEntries(innerFormData))
    const formDataJson= JSON.stringify(formData)
    console.log(innerFormDataJson, formDataJson)
    const csrfToken = store.token
    const axiosConfig = {headers: {"X-CSRFToken": csrfToken}}
    let response;
    try {
        response = await axios.post('/api/posts/create/', formDataJson, axiosConfig)
    } catch(error) {
        response = error.response
    }
    console.log(response)
    
}

</script>

<template>
    <form method="POST" action="/django/" @submit.prevent="handleSubmitForm">
        <div>
            <div>
            <input type="text" required v-model="formData.title" name="title" placeholder="Your blog title" v-on:keyup="handleAutoSlugChange"/>

        </div>
        <div>
            <input type="text" required v-model="formData.slug" name="slug" placeholder="your-blog-slug"/>

        </div>
        <div>
            <input type="text" required v-model="formData.slugger" name="slugger" placeholder="your-blog-slug"/>
        </div>
        <div>
            <p>Preview:</p>
            <p>Title: {{ formData.title  }}</p>
            <p>Slug: {{ formData.slug  }}</p>
            <button type="submit">Send</button>
        </div>
        </div>
    </form>
</template>
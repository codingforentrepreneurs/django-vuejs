<script setup>
import {reactive} from 'vue'
let formData = reactive({
    'title': '',
    'slug': '',
})
const handleAutoSlugChange = (event) =>{
    // console.log(formData.title)
    // console.log(event.target.value)
    // formData.slug = slugify(event.target.value)
    formData.slug = event.target.value
}

</script>

<template>
    <div>
        <div>
        <input type="text" v-model="formData.title" name="title" placeholder="Your blog title" v-on:keyup="handleAutoSlugChange"/>

    </div>
    <div>
        <input type="text" v-model="formData.slug" name="slug" placeholder="your-blog-slug"/>

    </div>
    <div>

        <p>Preview:</p>
        <p>Title: {{ formData.title  }}</p>
        <p>Slug: {{ formData.slug  }}</p>
    </div>
    </div>
</template>
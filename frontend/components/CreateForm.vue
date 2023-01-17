<script setup>
import {reactive} from 'vue'
let formData = reactive({
    'title': '',
    'slug': '',
})

</script>

<template>
    <div>
        <div>
        <input type="text" v-model="formData.title" name="title" placeholder="Your blog title"/>

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
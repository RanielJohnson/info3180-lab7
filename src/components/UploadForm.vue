<template>
    <form @submit.prevent= "uploadPhoto" method= "POST" id= "uploadForm" >       
        <div class="form-group">
            <label for="description">Description</label>
            <textarea class="form-control" id="description" rows="10" ></textarea>
        </div>  

        <div class="form-group">
            <label for="photo">Photo Upload</label>
            <input type="file" class="form-control-file" id="photo">
        </div>
    </form>
</template>

<script>
    export default {
        data() {
            return {
            };
        },
        uploadPhoto() {
            let uploadForm = document.getElementById('uploadForm');
            console.log(uploadForm)
            let form_data = new FormData(uploadForm);
            console.log(form_data)
            
            fetch("/api/upload", {
            method: 'POST',
            body: form_data,
            headers: {'X-CSRFToken': this.csrf_token}
            })
            .then(function (response) {
            return response.json();
            })
            .then(function (data) {
            // display a success message
            console.log(data);
            })
            .catch(function (error) {
            console.log(error);
            });
        },
 
    }
</script>

<style>
</style>
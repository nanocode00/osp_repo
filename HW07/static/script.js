function getImageFiles(e) {
	const files = e.currentTarget.files;
	console.log(typeof files, files);
}

const realUpload = document.querySelector('.real-upload');
const upload = document.querySelector('.upload');

upload.addEventListener('click', () => realUpload.click());
realUpload.addEventListener('change', getImageFiles);
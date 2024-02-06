export const removeEmptyUploads = async (list, formData) => {
    list.forEach(e => {
        const uploads = Array.from(formData.getAll(e));
        if (uploads[0].size === 0) {
            formData.delete(e)
        }
    })
}

document.body.addEventListener("keydown",(ev) => {
    if(ev.ctrlKey && ev.key === "b"){
        let arr = window.prompt("tags: ")
        let bookmark_obj = {"url": location.href, "time": Date.now(),"tags":arr}

        console.log(bookmark_obj)
    }
})




function change_background_color(){
    random_num =Math.floor(Math.random()*5)
    color_list =["#E91E63","#009688","#607D8B","#4FC3F7","#880E4F"]

    document.body.style.backgroundColor = color_list[random_num];
}
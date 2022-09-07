var switch_state = 'extended';
function extend_card_view_mob(){
    var whole_content_div = this.document.querySelector('.content-part');
    var parent_div = this.document.querySelector('.event');
    var arrow = this.document.querySelector('.extend-btn');
    var height_of_content_part = whole_content_div.style.height;
    var height_of_parent_div = parent_div.style.height;
    if (switch_state == 'extended'){
        whole_content_div.style.height = 'unset';
        whole_content_div.style.max-height = 'unset';
        parent_div.style.height = 'unset';
        parent_div.style.max-height = 'unset';
    }
    
    
}
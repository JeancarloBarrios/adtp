jQuery("#side-menu").click(function(e){
    
    e.preventDefault();
    
    if (jQuery("#sidebar-wrapper").hasClass("collapsed")){
        jQuery("#sidebar-wrapper").removeClass("collapsed");
        jQuery("#sidebar-wrapper").addClass("not-collapsed");
        jQuery("#side-menu").find($(".fa")).removeClass('fa-chevron-down').addClass('fa-chevron-right');
        jQuery("#sidebar-wrapper a.sidebar-text").removeClass("hidden");
        jQuery("#sidebar-wrapper a.sidebar-text").addClass("visible");


    }
    else if (jQuery("#sidebar-wrapper").hasClass("not-collapsed")){
        jQuery("#sidebar-wrapper").removeClass("not-collapsed");
        jQuery("#sidebar-wrapper").addClass("collapsed");
        jQuery(this).find($(".fa")).removeClass('fa-chevron-right').addClass('fa-chevron-down');
        jQuery("#sidebar-wrapper a.sidebar-text").removeClass("visible");
        jQuery("#sidebar-wrapper a.sidebar-text").addClass("hidden");


    }

});
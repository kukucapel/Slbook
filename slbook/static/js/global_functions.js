$(document).ready(function() {

  // Поиск на телефоне

  var clear_opacity = 0;
  
  var clear = $('.clear_button');

  $('#mobile_search_input').on('input', function() {

    if(clear_opacity == 0){

      clear.css('display','flex');
      clear.css('animation', 'show 0.3s ease-in-out');
      clear.css('animation-fill-mode', 'forwards');
      
      clear_opacity = 1;
    }

    var value = $(this).val().trim().toLowerCase();
    var options = $('.mobile_search_option');

    if(value != ''){
         options.each(function(){
          if($(this).text().toLowerCase().search(value) != -1){
            $(this).css('display', 'flex');
          }
          else{
            $(this).css('display', 'none');
          }
      })
    }
        else{
           options.each(function(){
            $(this).css('display', 'none');
            })

            clear.css('animation', 'hide 0.3s ease-in-out');
            clear.css('animation-fill-mode', 'forwards');
          
            setTimeout(function(){
              clear.css('display','none');
            }, 300);

            clear_opacity = 0;
    }

  });

  // Кнопка "Отчистить" на телефона

  clear.on('click', function(){

    let input = $('#mobile_search_input');

    input.css('animation', 'hide 0.3s ease-in-out');
    input.css('animation-fill-mode', 'forwards');

    $('.mobile_search_option').css('display','none');
    
    setTimeout(function(){
      input.val('');

      input.css('animation', 'show 0.3s ease-in-out');
      input.css('animation-fill-mode', 'forwards');

    }, 300);

    clear.css('animation', 'hide 0.3s ease-in-out');
    clear.css('animation-fill-mode', 'forwards');

    setTimeout(function(){
      clear.css('display','none');
    }, 300);

    clear_opacity = 0;


  });
 
  // Поиск на ПК
 
  $('#pc_search_input').on('input', function() {

    var value = $(this).val().trim().toLowerCase();
    var options = $('.search_option');

    if(value != ''){
         options.each(function(){
          if($(this).text().toLowerCase().search(value) != -1){
            $(this).css('display', 'flex');
          }
          else{
            $(this).css('display', 'none');
          }
      })
    }
        else{
           options.each(function(){
            $(this).css('display', 'none');
            })
    }

  });

  var eyesight_menu = $('.eyesight_instruments');
  var eye_buttons = $('.eyesight_button');

  $('.eyesight_container').on('click',function(){

    eyesight_menu.css('display', 'flex');
    eyesight_menu.css('opacity', '1');
    eyesight_menu.css('animation', 'show_eyesight 0.3s ease-in-out');
    eyesight_menu.css('animation-fill-mode', 'forwards');

    setTimeout(function(){

      eye_buttons.css('animation','show 0.3s ease-in-out');
      eye_buttons.css('animation-fill-mode', 'forwards');

    }, 300);


  });

  $('#eyesight_close').on('click',function(){

    eye_buttons.css('animation','hide 0.3s ease-in-out');
    eye_buttons.css('animation-fill-mode', 'forwards');
  
    setTimeout(function(){

      eyesight_menu.css('animation', 'hide_eyesight 0.3s ease-in-out');
      eyesight_menu.css('animation-fill-mode', 'forwards');

    }, 300);    
  })

  function change_style(id){

    const color_mass = {
      blue:'/static/css/global_styles_blue.css', 
      black:'/static/css/global_styles_black.css', 
      white:'/static/css/global_styles_white.css'
    };
  
    $('#styles_link').attr('href' , color_mass[id]);
  
  }

  $('#eyesight_black').on('click', function(){change_style('black')});
  $('#eyesight_blue').on('click', function(){change_style('blue')});
  $('#eyesight_white').on('click', function(){change_style('white')});


  var img_count = 0;

  function hide_show_img(id){
    
    const what_to_do = {
      hide:'0', 
      show:'1'
    };
  
    $('.picture').css('opacity', what_to_do[id]);

  }

  $('#eyesight_image').on('click', function(){
  
    if(img_count == 0){

      hide_show_img('hide');
      img_count = 1;

      return;
    }
    
    if(img_count == 1){
      
      hide_show_img('show');
      img_count = 0;

      return;
    }

  });


});




//анимация при загрузке страницы
function show_body(){

  var main_body = document.getElementById('wrapper');
  var loading = document.getElementById('loading');

  loading.style.animation = 'hide 0.3s ease-in-out';
  
  setTimeout(function(){
    loading.style.display = 'none';
    document.body.style.overflowY = 'auto';
  }, 300);

  main_body.style.animation = "show_body 2s";
  main_body.style.animationFillMode = "forwards";
}

//анимация при закрытии страницы

function close_page(){

  var main_body = document.getElementById('wrapper');

  main_body.style.animation = 'hide 0.5s ease-in-out';
  main_body.style.animationFillMode = "forwards";

}


// открытие мобильного меню

var ms_state = 0;

function show_mobile_menu(){

  var main_content = document.getElementById('main_content');
  var container = document.getElementById('mob_cont');
  var button = document.getElementById('mmb');

  if(ms_state == 0){

    document.body.style.overflowY = 'hidden';

    main_content.style.animation = 'hide 0.3s ease-in-out';
    main_content.style.animationFillMode = "forwards";

    setTimeout(function(){
      main_content.style.display= 'none';
    }, 300);

    container.style.display = "flex";
    container.style.animation = 'show 0.3s ease-in-out';
    container.style.animationFillMode = "forwards";

    button.style.backgroundImage='url(../img/mobile_menu_hover.png)';

    ms_state = 1;

    return;
  }
  
  if(ms_state == 1){

    document.body.style.overflowY = 'auto';

    main_content.style.display = 'flex';

    main_content.style.animation = 'show 0.3s ease-in-out';
    main_content.style.animationFillMode = "forwards";

    container.style.animation = 'hide 0.3s ease-in-out';
    container.style.animationFillMode = "forwards";

    button.style.backgroundImage='url(../img/mobile_menu.png)';

    setTimeout(function(){
      container.style.display = "none";
    }, 300);
   
    ms_state = 0;

    return;
  }

}



/* Открытие / закрытие пунктов мобильного меню */

var mobile_menu_state = [0,0,0,0,0,0];
var previous_id = 'none';

function mobile_menu(id){

  var option_id = 'option_' + id;
  var button_id = 'button_' + id;


  var search_container = document.getElementById('mobile_search_container');
  var option = document.getElementById(option_id);
  var button = document.getElementById(button_id);

  if(mobile_menu_state[id] == 0){

      if(previous_id != 'none'){
        mobile_menu_state[previous_id] = 0;

        let option_id = 'option_' + previous_id;
        let button_id = 'button_' + previous_id;
        let option = document.getElementById(option_id);
        let button = document.getElementById(button_id);

        option.style.display = 'none';
        button.style.backgroundColor = 'rgb(55, 184, 243)';  
        search_container.style = 'box-shadow: none';  
      }

    option.style.display = 'block';
    button.style.backgroundColor = 'rgb(19, 76, 133)';
    search_container.style = 'box-shadow: 0 0 5px rgba(0,0,0,0.5)';

    mobile_menu_state[id] = 1;

    previous_id = id;

    return;
  }

  
  if(mobile_menu_state[id] == 1){

    option.style.display = 'none';
    button.style.backgroundColor = 'rgb(55, 184, 243)';   
    search_container.style = 'box-shadow: none';  

    mobile_menu_state[id] = 0;

    return;
  }
}



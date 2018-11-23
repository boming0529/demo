odoo.define('bs_demo.website_signature', function (require) {
    'use strict';

    var ajax = require('web.ajax');

    $(function () {
        if ($('.panel-bs-signature').length > 0) {
            $.each($('.panel-bs-signature'), function () {
                var $container = $(this);
                var $sigdiv = $container.find('.bs_signature');
                $sigdiv = $sigdiv.jSignature({
                    'decor-color': '#D1D0CE',
                    'color': '#000',
                    'background-color': '#fff',
                    'UndoButton': true
                });
                var $clearbtn = $container.find('.sign_clean');
                var $acceptbtn = $container.find('.sign_accept');
                $clearbtn.on('click', function () {
                    $sigdiv.jSignature('reset');
                    var signature_input = $container.find('input.hidden');
                    signature_input.val('');
                });
                $acceptbtn.on('click', function () {
                    var empty_sign = $sigdiv.jSignature("getData", 'image');
                    var signature_input = $container.find('input.hidden');
                    signature_input.val(empty_sign[1] + '');
                });
            });
        }
    });
});
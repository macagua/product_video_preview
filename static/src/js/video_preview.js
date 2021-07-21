/**
 * @author Cybrosys Technologies - info@cybrosys.com
 * @maintainer Leonardo Caballero - leonardo@pidela.cl
 *
 * Displays preview of the video showcasing product.
 *
 */

odoo.define('product_video_preview.video_field_preview', function (require) {
    'use strict';


    var AbstractField = require('web.AbstractField');
    var core = require('web.core');
    var fieldRegistry = require('web.field_registry');
    var QWeb = core.qweb;

    // extending the FieldVideoPreview
    var FieldVideoPreview = AbstractField.extend({
        className: 'd-block o_field_video_preview',

        _render: function () {
            this.$el.html(QWeb.render('productVideo', {
                embedCode: this.value,
            }));
        },
    });

    // registry the FieldVideoPreview
    fieldRegistry.add('video_preview', FieldVideoPreview);
    return FieldVideoPreview;
});



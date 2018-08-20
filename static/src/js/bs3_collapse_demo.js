odoo.define('bs3_collapse_demo', function (require) {
    'use strict';
    var options = require('web_editor.snippets.options');

    options.registry.collapse_demo = options.Class.extend({
        start: function () {
            var self = this;
            this.$el.find(".js_add").on("click", _.bind(this._add_new_tab, this));
            this.$el.find(".js_remove").on("click", _.bind(this._remove_current_tab, this));
            this._super();
        },
        create_collapse_ids: function ($target) {
            var time = new Date().getTime();
            var $tab = $target.find('[data-toggle="collapse"]');
            // link to the parent group
            var $tablist = $target.closest('.panel-group');
            var tablist_id = $tablist.attr("id");
            if (!tablist_id) {
                tablist_id = "bs3Collapse" + time;
                $tablist.attr("id", tablist_id);
            }
            $tab.attr('data-parent', "#" + tablist_id);
            // link to the collapse
            var $panel = $target.find('.panel-collapse');
            $panel.each(function(index, item) {
                var $item = $(item);
                time++;
                panel_id = "bs3CollapseTab" + time;
                $item.attr("id", panel_id);
                var $tab = $item.closest('.panel-default').find('.panel-heading')
                $tab.attr('data-target', "#" + panel_id);
            });
        },
        drop_and_build_snippet: function () {
            this._super();
            this.create_collapse_ids(this.$target);
        },
        _add_new_tab: function () {
            var self = this;
            var time = new Date().getTime();
            var $tablist = self.$target.find('.panel-group');
            var tablist_id = $tablist.attr("id");
            var new_content = $('<div/>', {
                'class': 'panel panel-default'
            })
            var head = $('<div/>', {
                'class': "panel-heading",
                'data-toggle': "collapse",
                'role': 'tab',
                'data-parent': '#'+ tablist_id,
                'data-target': '#bs3CollapseTab' + time
            });
            var title = $('<h4/>', {
                'class': 'panel-title',
                'text': 'bs-demo',
            })
            head.append(title);
            new_content.append(head);

            var tabpanel = $('<div/>', {
                role: 'tabpanel',
                id: 'bs3CollapseTab' + time,
                class: 'panel-collapse collapse'
            });
            var panelbody = $('<div/>', {
                    class: "panel-body"
                })
                .append($('<p/>').html('your desrcipt here'))
                .append($('<p/>').html('your desrcipt here'))
            tabpanel.append(panelbody)
            new_content.append(tabpanel);
            $tablist.append(new_content)
        },
        _remove_current_tab: function () {
            var self = this;
            var $tablist = self.$target.find('.panel-group');
            // aria-expanded
            if ($tablist.find('> div.panel-default').size() > 1 && $tablist.find('div[aria-expanded="true"]').length > 1) {
                $tablist.find('div[aria-expanded="true"]').closest('div.panel-default').remove();
            }
        },
    })
});
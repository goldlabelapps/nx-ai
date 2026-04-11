
from app.utils.db import get_db_connection_direct


# Combined schema: magento_products + custom orders fields
ORDERS_TABLE_SCHEMA = '''
CREATE TABLE orders (
    sku TEXT PRIMARY KEY,
    store_view_code TEXT,
    attribute_set_code TEXT,
    product_type TEXT,
    categories TEXT,
    product_websites TEXT,
    name TEXT,
    description TEXT,
    short_description TEXT,
    weight NUMERIC,
    product_online BOOLEAN,
    tax_class_name TEXT,
    visibility TEXT,
    price NUMERIC,
    special_price NUMERIC,
    special_price_from_date DATE,
    special_price_to_date DATE,
    url_key TEXT,
    meta_title TEXT,
    meta_keywords TEXT,
    meta_description TEXT,
    base_image TEXT,
    base_image_label TEXT,
    small_image TEXT,
    small_image_label TEXT,
    thumbnail_image TEXT,
    thumbnail_image_label TEXT,
    swatch_image TEXT,
    swatch_image_label TEXT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    new_from_date DATE,
    new_to_date DATE,
    display_product_options_in TEXT,
    map_price NUMERIC,
    msrp_price NUMERIC,
    map_enabled TEXT,
    gift_message_available TEXT,
    custom_design TEXT,
    custom_design_from DATE,
    custom_design_to DATE,
    custom_layout_update TEXT,
    page_layout TEXT,
    product_options_container TEXT,
    msrp_display_actual_price_type TEXT,
    country_of_manufacture TEXT,
    additional_attributes TEXT,
    qty NUMERIC,
    out_of_stock_qty NUMERIC,
    use_config_min_qty BOOLEAN,
    is_qty_decimal BOOLEAN,
    allow_backorders BOOLEAN,
    use_config_backorders BOOLEAN,
    min_cart_qty NUMERIC,
    use_config_min_sale_qty BOOLEAN,
    max_cart_qty NUMERIC,
    use_config_max_sale_qty BOOLEAN,
    is_in_stock BOOLEAN,
    notify_on_stock_below BOOLEAN,
    use_config_notify_stock_qty BOOLEAN,
    manage_stock BOOLEAN,
    use_config_manage_stock BOOLEAN,
    use_config_qty_increments BOOLEAN,
    qty_increments NUMERIC,
    use_config_enable_qty_inc BOOLEAN,
    enable_qty_increments BOOLEAN,
    is_decimal_divided BOOLEAN,
    website_id TEXT,
    related_skus TEXT,
    related_position TEXT,
    crosssell_skus TEXT,
    crosssell_position TEXT,
    upsell_skus TEXT,
    upsell_position TEXT,
    additional_images TEXT,
    additional_image_labels TEXT,
    hide_from_product_page TEXT,
    custom_options TEXT,
    bundle_price_type TEXT,
    bundle_sku_type TEXT,
    bundle_price_view TEXT,
    bundle_weight_type TEXT,
    bundle_values TEXT,
    bundle_shipment_type TEXT,
    associated_skus TEXT,
    downloadable_links TEXT,
    downloadable_samples TEXT,
    configurable_variations TEXT,
    configurable_variation_labels TEXT,
    hide BOOLEAN DEFAULT FALSE,
    flag BOOLEAN DEFAULT FALSE
);
'''

def recreate_orders_table():
    conn = get_db_connection_direct()
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS orders;')
    cur.execute(ORDERS_TABLE_SCHEMA)
    conn.commit()
    cur.close()
    conn.close()
    print('orders table recreated.')

if __name__ == '__main__':
    recreate_orders_table()

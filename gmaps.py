AIzaSyANp-v7jK0OVVUcjx62E8k1pnJQdoGHako


starbucks_df = df[df['chain_name'] == 'starbucks']
starbucks_df = starbucks_df[['latitude', 'longitude']]

starbucks_layer = gmaps.symbol_layer(
    starbucks_df, fill_color="green", stroke_color="green", scale=2
)
fig = gmaps.figure()
fig.add_layer(starbucks_layer)
fig

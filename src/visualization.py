from pathlib import Path
import folium
import plotly.express as px

def poi_map(pois, output_path):
    m = folium.Map(location=[pois.geometry.y.mean(), pois.geometry.x.mean()], zoom_start=13, tiles="OpenStreetMap")
    for _, row in pois.iterrows():
        folium.CircleMarker([row.geometry.y, row.geometry.x], radius=4,
                            tooltip=f"{row.get('name','Unnamed')} | {row.get('service_type','')}").add_to(m)
    Path(output_path).parent.mkdir(parents=True, exist_ok=True); m.save(output_path)

def accessibility_map(origins, accessibility, output_path):
    frame = origins.copy(); frame["travel_time_min"] = accessibility["travel_time_min"].values
    m = folium.Map(location=[frame.geometry.y.mean(), frame.geometry.x.mean()], zoom_start=13)
    for _, row in frame.iterrows():
        if row["travel_time_min"] != float("inf"):
            folium.CircleMarker([row.geometry.y, row.geometry.x], radius=3,
                                tooltip=f"{row['travel_time_min']:.1f} min").add_to(m)
    Path(output_path).parent.mkdir(parents=True, exist_ok=True); m.save(output_path)

def travel_time_plot(df, output_path):
    fig = px.histogram(df, x="travel_time_min", nbins=30, title="Network travel-time distribution")
    Path(output_path).parent.mkdir(parents=True, exist_ok=True); fig.write_html(output_path)

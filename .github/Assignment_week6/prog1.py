
import pandas as pd
import matplotlib.pyplot as plt

class CovidVisualization:

    def __init__(self, file):
        self.df = pd.read_csv(file)

    # 1 Bar Chart – Top 10 Countries by Confirmed Cases
    def bar_top10_confirmed(self):

        top10 = self.df.nlargest(10, "Confirmed")
        plt.figure()
        plt.bar(top10["Country/Region"], top10["Confirmed"], color="skyblue")
        plt.title("Top 10 Countries by Confirmed Cases")
        plt.xlabel("Country")
        plt.ylabel("Confirmed Cases")
        plt.tight_layout()
        plt.show()

    # 2 Pie Chart – Global Death Distribution by Region
    def pie_deaths_region(self):

        deaths = self.df.groupby("WHO Region")["Deaths"].sum()
        plt.figure()
        plt.pie(deaths, labels=deaths.index, autopct="%1.1f%%", startangle=90)
        plt.title("Global Death Distribution by Region")
        plt.show()

    # 3 Line Chart – Confirmed vs Deaths (Top 5 Countries)
    def line_confirmed_deaths(self):

        top5 = self.df.nlargest(5, "Confirmed")
        plt.figure()
        plt.plot(top5["Country/Region"],top5["Confirmed"],marker="o",label="Confirmed",color="blue")
        plt.plot(top5["Country/Region"],top5["Deaths"],marker="o",label="Deaths",color="red")
        plt.title("Confirmed vs Deaths (Top 5 Countries)")
        plt.xlabel("Country")
        plt.ylabel("Cases")
        plt.legend()
        plt.tight_layout()
        plt.show()

    # 4 Scatter Plot – Confirmed vs Recovered
    def scatter_confirmed_recovered(self):

        plt.figure()
        plt.scatter(self.df["Confirmed"],self.df["Recovered"],color="blue",alpha=0.6,edgecolors="black")
        plt.xlabel("Confirmed Cases")
        plt.ylabel("Recovered Cases")
        plt.title("Scatter Plot of Confirmed Cases vs Recovered Cases")
        plt.tight_layout()
        plt.show()

    # 5 Histogram – Death Counts across all countries
    def histogram_deaths(self):

        plt.figure()
        plt.hist(self.df["Deaths"],bins=10,edgecolor="black",color="orange")
        plt.title("Distribution of Death Counts")
        plt.xlabel("Deaths")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.show()

    # 6 Stacked Bar Chart – Confirmed, Deaths, Recovered (Top 5 Countries)
    def stacked_bar_top5(self):

        top5 = self.df.nlargest(5, "Confirmed")
        countries = top5["Country/Region"]
        confirmed = top5["Confirmed"]
        deaths = top5["Deaths"]
        recovered = top5["Recovered"]

        plt.figure(figsize=(8,5))
        plt.bar(countries, confirmed, color="blue")
        plt.bar(countries, deaths, bottom=confirmed, color="red")
        plt.bar(countries, recovered, bottom=confirmed + deaths, color="green")
        plt.xlabel("Countries")
        plt.ylabel("Number of Cases")
        plt.title("Confirmed, Deaths, Recovered (Top 5 Countries)")
        plt.legend(["Confirmed", "Deaths", "Recovered"])
        plt.tight_layout()
        plt.show()

    # 7 Box Plot – Confirmed Cases across Regions
    def boxplot_regions(self):

        data = self.df.groupby("WHO Region")["Confirmed"].apply(list)
        plt.figure()
        plt.boxplot(data, labels=data.index)
        plt.title("Confirmed Cases Distribution by Region")
        plt.ylabel("Confirmed Cases")
        plt.tight_layout()
        plt.show()

    # 8 Trend Comparison – India vs another country
    def india_vs_country(self, country):

        data = self.df[self.df["Country/Region"].isin(["India", country])]
        plt.figure(figsize=(6,5))
        plt.bar(data["Country/Region"],data["Confirmed"],color=["green", "purple"])
        plt.title(f"Confirmed Cases: India vs {country}")
        plt.ylabel("Confirmed Cases")
        plt.xlabel("Country")
        plt.tight_layout()
        plt.show()

# Run Visualizations
viz = CovidVisualization(".github/Assignment_week6/country_wise_latest.csv")
viz.bar_top10_confirmed()
viz.pie_deaths_region()
viz.line_confirmed_deaths()
viz.scatter_confirmed_recovered()
viz.histogram_deaths()
viz.stacked_bar_top5()
viz.boxplot_regions()
viz.india_vs_country("Brazil")
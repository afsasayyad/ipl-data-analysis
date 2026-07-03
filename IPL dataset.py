import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\THINK PAD\Downloads\archive (4)\matches.csv")
print(df.head(5))
print(df.columns.tolist())
print(df.shape)
print(df.isnull().sum())
df.drop(columns=["umpire3"],inplace=True)
df.dropna(subset=["winner","player_of_match"],inplace=True)
print(df.shape)
print(df["winner"].value_counts().head(10))
print(df["player_of_match"].value_counts().head(10))
df["toss_match_win"] = df["toss_winner"]==df["winner"]
print(df["toss_match_win"].value_counts())

#SQL
print("SQL")
conn = sqlite3.connect("ipl.db")
df.to_sql("ipl",conn,index=False,if_exists="replace")
result = pd.read_sql_query(""" SELECT player_of_match,COUNT(*) as awards
                           FROM ipl
                           GROUP BY player_of_match
                           ORDER BY awards DESC
                           LIMIT 10""",conn)
print(result)
#matplotlib
top_players = df["player_of_match"].value_counts().head(10)
plt.figure(figsize=(10,6))
top_players.plot(kind="bar",color=["gold","silver","peru","steelblue","crimson","mediumseagreen","darkorange","mediumpurple","tomato","teal"])
plt.title("Top 10 player of Match - IPL")
plt.xlabel("Player")
plt.ylabel("Awards")
plt.xticks(rotation=45,ha="right")
plt.tight_layout()
plt.savefig("top_player.png")
plt.show() 
top_teams = df["winner"].value_counts().head(10)
plt.figure(figsize=(10,6))
top_teams.plot(kind="bar",color=["crimson","darkorange","gold","mediumseagreen","steelblue","mediumpurple","tomato","teal","peru","silver"])
plt.title("Most Wins by Team - IPL")
plt.xlabel("Team")
plt.ylabel("Wins")
plt.xticks(rotation=45,ha="right")
plt.tight_layout()
plt.savefig("top_team.png")
plt.show() 

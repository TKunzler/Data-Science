import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.ticker import PercentFormatter
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns
import os
import numpy as np
from matplotlib import gridspec
from PIL import Image, ImageDraw, ImageFont


os.environ["OMP_NUM_THREADS"] = "9"


#Colors for charts
color_points_bg = '#41210A'
color_points_lt = '#FBB03B'
color_gols_bg = '#567D6B'
color_gols_lt = 'white'
color_assits_bg = '#9F6923'
color_assits_lt = 'white' 

# Colors alternate rows
row_colors = ['#DDB06D', '#EBCFA7'] 



def plot_season_standings_table(df_players):
    
    # Create a figure and axis for the table
    fig, ax = plt.subplots(figsize=(3.5, 3)) 
    ax.axis('off')  # Disable the axes

    # Create a table
    table = ax.table(cellText=df_players.values, colLabels=df_players.columns, cellLoc='center', loc='center')

    # Table styling
    table.auto_set_font_size(False) 
    table.set_fontsize(10)
    table.scale(3.5, 3.5)  # Adjust the scale
    table.scale(0.85, 0.5)  # Adjust the scale to reduce space between rows

    # Highlight the first row with a different color
    for i in range(len(df_players.columns)):
        cell = table[(0, i)]
        cell.set_facecolor(color_points_bg)  # Background color
        cell.get_text().set_color(color_points_lt)  # Text color
        cell.get_text().set_weight('bold')  # Bold text

    # Alternate row colors for better visualization
    for i in range(len(df_players)):
        for j in range(len(df_players.columns)):
            table[(i + 1, j)].set_facecolor(row_colors[i % 2])

    # Bold the sixth column
    for i in range(len(df_players)):
        table[(i + 1, 6)].get_text().set_weight('bold')

    # Display the table
    plt.show()




def plot_points_evolution(df_vd, player_names):
 
    # Plot the points of each player by date
    plt.figure(figsize=(20, 10))

    for player in player_names:
        plt.plot(df_vd['Date'], df_vd[player + '_points'], label=player, linewidth=5)  

    # Remove the top, right, and bottom borders
    sns.despine(top=True, right=True, left=True, bottom=True)    

    # Remove the grid
    plt.grid(False)

    # Set the title and labels
    plt.title('Score Evolution Throughout the Year', fontsize=20, weight='bold')
    plt.xlabel('Date')
    plt.ylabel('Score')
    
    # Add legend
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)
    
    # Adjust layout to fit elements
    plt.tight_layout()
    
    # Display the plot
    plt.show()



def plot_goal_scorers(df):
    
    # Count occurrences of each player in the 'Scorer' column
    count_scorer = df['Scorer'].value_counts()
    
    # Filter players with more than 10 goals
    count_scorers = count_scorer[count_scorer > 10]
    
    # Create a horizontal bar chart
    plt.figure(figsize=(12, 7))

    # Define the starting color and the lighter color
    start_color = "#567D6B"
    end_color = "#9CBAAC"

    # Number of bars you have
    num_bars = len(count_scorers)

    # Create a custom color palette
    colors = [start_color, end_color]
    cmap = LinearSegmentedColormap.from_list("custom_green", colors, N=num_bars)
    custom_palette = [cmap(i/num_bars) for i in range(num_bars)]

    # Display the bar plot with the custom palette
    sns.barplot(x=count_scorers.values, y=count_scorers.index, palette=custom_palette)
    
    # Add labels and title
    plt.title('Number of Goals per Player (Above 10 Goals)', fontsize=16, weight='bold')
    
    # Add the number of goals on each bar
    for i, v in enumerate(count_scorers.values):
        plt.text(v + 0.1, i, str(v), color='black', va='center', weight='bold', size=11)
    
    # Remove borders
    sns.despine(left=False, right=True, top=True, bottom=True)
    
    # Remove the x-axis legend
    plt.xticks([])    
    
    # Adjust the font size of y-axis items
    plt.tick_params(axis='y', labelsize=10)
    
    # Show the graph
    plt.show()



def plot_assist_leaders(assistant_counts):
    # Plotting the Graph
    # Filter assistants with more than 10 assists
    assistant_counts = assistant_counts[assistant_counts > 10]

    # Create a horizontal bar chart
    plt.figure(figsize=(12, 7))

    # Define the starting color and the lighter color
    start_color = "#9F6923"
    end_color = "#E0B172"

    # Number of bars you have
    num_bars = len(assistant_counts)

    # Create a custom color palette
    colors = [start_color, end_color]
    cmap = LinearSegmentedColormap.from_list("custom_green", colors, N=num_bars)
    custom_palette = [cmap(i/num_bars) for i in range(num_bars)]

    sns.barplot(x=assistant_counts.values, y=assistant_counts.index, palette=custom_palette)

    # Add labels and title
    plt.title('Number of Assists per Player (More than 10 Assists)', fontsize=16, weight='bold')

    # Add the number of assists to each bar
    for i, v in enumerate(assistant_counts.values):
        plt.text(v + 0.1, i, str(v), color='black', va='center', weight='bold', size=11)

    # Remove borders
    sns.despine(left=False, right=True, top=True, bottom=True)

    # Remove the x-axis legend
    plt.xticks([])

    # Adjust the font of the y-axis items
    plt.tick_params(axis='y', labelsize=10)

    # Show the chart
    plt.show()



def plot_assistants_scorers_tables(df_assistants, df_scorer):
    # Create a figure and axes for the subplots
    fig, axs = plt.subplots(1, 2, figsize=(8, 4))

    # Disable the axes in both subplots
    for ax in axs:
        ax.axis('off')

    # Table 1: Assistants Table
    table1 = axs[0].table(cellText=df_assistants.values, colLabels=df_assistants.columns, cellLoc='center', loc='upper center')
    table1.auto_set_font_size(False)
    table1.set_fontsize(10)
    table1.scale(3.4, 3.4)  # Adjust the scale
    table1.scale(0.95, 0.5)  # Adjust the scale to reduce space between rows

    # Highlight the first row with a different color and text color for Assistants Table
    for i in range(len(df_assistants.columns)):
        cell = table1[(0, i)]
        cell.set_facecolor(color_assits_bg)  # Background color
        cell.get_text().set_color(color_assits_lt)  # Text color
        cell.get_text().set_weight('bold')  # Bold text

    # Alternate row colors for better visualization in Assistants Table
    for i in range(len(df_assistants)):
        for j in range(len(df_assistants.columns)):
            table1[(i + 1, j)].set_facecolor(row_colors[i % 2])

    # Bold the fourth column in Assistants Table
    for i in range(len(df_assistants)):
        table1[(i + 1, 3)].get_text().set_weight('bold')

    # Title for Table 1
    axs[0].set_title('Assistants Table', fontsize=14, fontweight='bold', color=color_assits_bg, pad=10)    

    # Table 2: Scorer Table
    table2 = axs[1].table(cellText=df_scorer.values, colLabels=df_scorer.columns, cellLoc='center', loc='upper center')
    table2.auto_set_font_size(False)
    table2.set_fontsize(10)
    table2.scale(3.4, 3.4)  # Adjust the scale
    table2.scale(0.95, 0.5)  # Adjust the scale to reduce space between rows

    # Highlight the first row with a different color and text color for Scorer Table
    for i in range(len(df_scorer.columns)):
        cell = table2[(0, i)]
        cell.set_facecolor(color_gols_bg)  # Background color
        cell.get_text().set_color(color_gols_lt)  # Text color
        cell.get_text().set_weight('bold')  # Bold text

    # Alternate row colors for better visualization in Scorer Table
    for i in range(len(df_scorer)):
        for j in range(len(df_scorer.columns)):
            table2[(i + 1, j)].set_facecolor(row_colors[i % 2])

    # Bold the fourth column in Scorer Table
    for i in range(len(df_scorer)):
        table2[(i + 1, 3)].get_text().set_weight('bold')

    # Manually adjust the margins
    plt.subplots_adjust(wspace=2.45)  # Adjust the space between the subplots

    # Title for Table 2
    axs[1].set_title('Scorer Table', fontsize=14, fontweight='bold', color=color_gols_bg , pad=10)

    # Display the tables together
    plt.show()



def plot_goals_per_location(df_sum_goals_venues):
    wid = 0.5

    # Create side-by-side subplots
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 6))

    # Bar chart for the total number of matches by venue
    bars1 = ax1.bar(df_sum_goals_venues['Location'].values, df_sum_goals_venues['Number of Matches'].values, color='#BD812B', width=wid)
    ax1.set_title('Number of Matches per Location', fontsize=20, weight='bold')
    ax1.set_yticks([])  # Remove y-axis labels

    # Add values on top of the bars
    for bar in bars1:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom', fontweight='bold', fontsize=14)

    # Bar chart for the total number of goals by venue
    bars2 = ax2.bar(df_sum_goals_venues['Location'], df_sum_goals_venues['Total Goals'], color='#64946E', width=wid)
    ax2.set_title('Number of Goals per Location', fontsize=20, weight='bold')
    ax2.set_yticks([])  # Remove y-axis labels

    # Add values on top of the bars
    for bar in bars2:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom', fontweight='bold', fontsize=14)

    # Bar chart for the average number of goals by venue
    bars3 = ax3.bar(df_sum_goals_venues['Location'], df_sum_goals_venues['Average'], color='#80511B', width=wid)
    ax3.set_title('Average Goals per Location', fontsize=20, weight='bold')
    ax3.set_yticks([])  # Remove y-axis labels

    # Add values on top of the bars
    for bar in bars3:
        yval = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom', fontweight='bold', fontsize=14)

    # Remove borders from the plots
    for ax in [ax1, ax2, ax3]:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)

    # Set Y-axis limits
    ax1.set_ylim(bottom=0, top=30)  # Adjust as needed
    ax2.set_ylim(bottom=0, top=750)  # Adjust as needed
    ax3.set_ylim(bottom=0, top=35)  # Adjust as needed

    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Set X-axis labels to bold
    ax1.set_xticks(ax1.get_xticks())
    ax1.set_xticklabels(ax1.get_xticklabels(), fontweight='bold')

    ax2.set_xticks(ax2.get_xticks())
    ax2.set_xticklabels(ax2.get_xticklabels(), fontweight='bold')

    ax3.set_xticks(ax3.get_xticks())
    ax3.set_xticklabels(ax3.get_xticklabels(), fontweight='bold')

    # Display the plots
    plt.show()



def plot_monthly_tables(table_month, table_goals_month, table_assists_month, months_eng, selected_month):
    # Create a grid with 1 row and 3 columns to accommodate the 3 tables
    gs = gridspec.GridSpec(1, 3, width_ratios=[1, 1, 1])

    # Create a figure with the grid
    fig = plt.figure(figsize=(15, 5))

    # Add the first table to the axis of the first column
    ax0 = plt.subplot(gs[0])
    ax0.axis('off')
    table0 = ax0.table(cellText=table_month.values, colLabels=table_month.columns, loc='center', cellLoc='center', colColours=[color_points_bg]*len(table_month.columns))
    table0.auto_set_font_size(False)
    table0.set_fontsize(13)
    table0.auto_set_column_width(col=list(range(len(table_month.columns))))
    table0.scale(1, 1.5)  # Adjust the value as needed
    ax0.text(0.5, 0.90, f'Points Table - {months_eng[selected_month]}', fontsize=14, ha='center', va='center', color=color_points_bg, fontweight='bold', transform=ax0.transAxes)

    # Change the color of the first row text for the first table
    for i in range(len(table_month.columns)):
        cell = table0[(0, i)]
        cell.get_text().set_color(color_points_lt)  # Text color

    # Alternate row colors for the first table
    for i in range(len(table_month)):
        for j in range(len(table_month.columns)):
            table0[(i + 1, j)].set_facecolor(row_colors[i % 2])

    # Add the second table to the axis of the second column
    ax1 = plt.subplot(gs[1])
    ax1.axis('off')
    table1 = ax1.table(cellText=table_goals_month.values, colLabels=table_goals_month.columns, loc='center', cellLoc='center', colColours=[color_gols_bg]*len(table_goals_month.columns))
    table1.auto_set_font_size(False)
    table1.set_fontsize(13)
    table1.auto_set_column_width(col=list(range(len(table_goals_month.columns))))
    table1.scale(1, 1.5)  # Adjust the value as needed
    ax1.text(0.5, 0.90, f'Goals Table - {months_eng[selected_month]}', fontsize=14, ha='center', va='center', color=color_gols_bg, fontweight='bold', transform=ax1.transAxes)

    # Alternate row colors for the second table
    for i in range(len(table_goals_month)):
        for j in range(len(table_goals_month.columns)):
            table1[(i + 1, j)].set_facecolor(row_colors[i % 2])

    # Change the color of the first row text for the second table
    for i in range(len(table_goals_month.columns)):
        cell = table1[(0, i)]
        cell.get_text().set_color(color_gols_lt)  # Text color        

    # Add the third table to the axis of the third column
    ax2 = plt.subplot(gs[2])
    ax2.axis('off')
    table2 = ax2.table(cellText=table_assists_month.values, colLabels=table_assists_month.columns, loc='center', cellLoc='center', colColours=[color_assits_bg]*len(table_assists_month.columns))
    table2.auto_set_font_size(False)
    table2.set_fontsize(13)
    table2.auto_set_column_width(col=list(range(len(table_assists_month.columns))))
    table2.scale(1, 1.5)  # Adjust the value as needed
    ax2.text(0.5, 0.90, f'Assists Table - {months_eng[selected_month]}', fontsize=14, ha='center', va='center', color=color_assits_bg, fontweight='bold', transform=ax2.transAxes)

    # Alternate row colors for the third table
    for i in range(len(table_assists_month)):
        for j in range(len(table_assists_month.columns)):
            table2[(i + 1, j)].set_facecolor(row_colors[i % 2])

    # Change the color of the first row text for the third table
    for i in range(len(table_assists_month.columns)):
        cell = table2[(0, i)]
        cell.get_text().set_color(color_assits_lt)  # Text color        

    # Adjust layout
    plt.tight_layout()
    plt.show()



def plot_games_goals_month(months_pt,goals_per_month, games_per_month):
    # Width of the bars
    wid = 0.7

    # Create side-by-side subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

    # Bar chart for total games per month
    bars1 = ax1.bar(months_pt, games_per_month, color='#BD812B', width=wid) 
    ax1.set_title('Number of Games per Month', fontsize=20, weight='bold')
    ax1.set_yticks([])  # Remove y-axis labels

    # Add values on top of the bars
    for bar in bars1:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom', fontweight='bold', fontsize=12)

    # Modify x-axis ticks
    ax1.set_xticks(months_pt)
    ax1.set_xticklabels(months_pt, fontweight='bold', fontsize=14)

    # Bar chart for number of goals per month
    bars2 = ax2.bar(months_pt, goals_per_month, color='#9B735A', width=wid)
    ax2.set_title('Number of Goals per Month', fontsize=20, weight='bold')
    ax2.set_yticks([])  # Remove y-axis labels

    # Add values on top of the bars
    for bar in bars2:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom', fontweight='bold', fontsize=10)

    # Modify x-axis ticks
    ax2.set_xticks(months_pt)
    ax2.set_xticklabels(months_pt, fontweight='bold', fontsize=14)

    # Remove borders from the plots
    for ax in [ax1, ax2]:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)

    # Set y-axis limits
    ax1.set_ylim(bottom=0, top=6)  # Adjust as needed
    ax2.set_ylim(bottom=0, top=185)  # Adjust as needed

    # Adjust layout to avoid overlap
    plt.tight_layout()

    # Show the plots
    plt.show()



def plot_average_goals_month(months_pt, average_goals_per_game):
    # Adjust the figure size
    plt.figure(figsize=(12, 6))

    # Create the line plot
    plt.plot(months_pt, average_goals_per_game, marker='o', color='#41210A', linewidth=2.5)  # Adjust linewidth as needed
    plt.title('Average Goals per Month', fontsize=20, weight='bold')

    # Set y-axis limits
    plt.ylim(bottom=0)
    plt.ylim(top=50)

    # Remove borders
    sns.despine(left=True, right=True, top=True, bottom=False)

    # Add values to each point on the plot
    for month, avg_goals in zip(months_pt, average_goals_per_game):
        plt.text(month, avg_goals - 2, f'{avg_goals:.2f}', ha='center', va='bottom', fontweight='bold', fontsize=10)

    # Remove y-axis ticks
    plt.yticks([])

    # Set y-axis limits to start at 15 and top at 45
    plt.ylim(bottom=15, top=45)  # Adjust as needed

    # Make x-axis tick labels bold
    plt.xticks(fontweight='bold')

    # Remove background grid lines
    plt.grid(False)

    # Display the plot
    plt.show()



def plot_goal_type(goal_type_counts):

    # Adjust the figure size
    plt.figure(figsize=(12, 6))

    # Plot the bar chart
    bars = plt.bar(goal_type_counts.index, goal_type_counts.values, color=['#41210A', '#613A13', '#80511B', '#9F6923', '#BD812B'])
    plt.title('Distribution of Goal Types', fontsize=20, weight='bold')

    # Add numbers above each bar with increased font size, bold, and the color of the bar
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, round(yval, 1),
                 ha='center', va='bottom', fontsize=15, weight='bold')

    # Remove borders
    sns.despine(left=True, right=True, top=True, bottom=False)

    # Modify the x-axis labels
    plt.xticks(fontweight='bold', fontsize=14)

    # Set the y-axis limit
    plt.ylim(0, 520)

    # Remove background grid lines
    plt.grid(False)

    # Remove the x-axis legend
    plt.yticks([])  

    plt.show()



def plot_goal_time(segment_counts):
    # Adjust the figure size
    plt.figure(figsize=(12, 6))

    # Plot the bar chart
    bars = plt.bar(segment_counts.index, segment_counts.values, color=['#FBB03B', '#BD812B', '#80511B'], width=0.5)
    plt.title('Distribution of Goals by Match Segment', fontsize=20, weight='bold')

    # Add the numbers on top of each bar
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, round(yval, 1),
                 ha='center', va='bottom', fontsize=15, weight='bold')

    # Remove borders
    sns.despine(left=True, right=True, top=True, bottom=False)

    # Remove y-axis ticks
    plt.yticks([])  

    # Adjust x-axis ticks
    plt.xticks(fontweight='bold', fontsize=15)

    # Remove background grid lines
    plt.grid(False)

    # Set the y-axis limit
    plt.ylim(0, 450)

    plt.show()



def plot_top_performances(top_10_scorers, top_10_assistants):
    # Create a grid of 1 row and 2 columns to accommodate the 2 tables
    gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1])

    # Create a figure with the grid
    fig = plt.figure(figsize=(15, 5))

    # Add the first table to the first column's axis
    ax0 = plt.subplot(gs[0])
    ax0.axis('off')
    table0 = ax0.table(cellText=top_10_scorers.values, colLabels=top_10_scorers.columns, loc='center', cellLoc='center', colColours=[color_gols_bg]*len(top_10_scorers.columns))
    table0.auto_set_font_size(False)
    table0.set_fontsize(15)
    table0.auto_set_column_width(col=list(range(len(top_10_scorers.columns))))
    table0.scale(2, 2.2)  # Adjust value as needed
    ax0.text(0.5, 1.20, f'Top Number of Goals in a Match', fontsize=20, ha='center', va='center', color=color_gols_bg, fontweight='bold', transform=ax0.transAxes)

    # Alternate row colors for the first table
    for i in range(len(top_10_scorers)):
        for j in range(len(top_10_scorers.columns)):
            table0[(i + 1, j)].set_facecolor(row_colors[i % 2])

    # Add the second table to the second column's axis
    ax1 = plt.subplot(gs[1])
    ax1.axis('off')
    table1 = ax1.table(cellText=top_10_assistants.values, colLabels=top_10_assistants.columns, loc='center', cellLoc='center', colColours=[color_assits_bg]*len(top_10_assistants.columns))
    table1.auto_set_font_size(False)
    table1.set_fontsize(15)
    table1.auto_set_column_width(col=list(range(len(top_10_assistants.columns))))
    table1.scale(2, 2.2)  # Adjust value as needed
    ax1.text(0.5, 1.20, f'Top Number of Assists in a Match', fontsize=20, ha='center', va='center', color=color_assits_bg, fontweight='bold', transform=ax1.transAxes)

    # Alternate row colors for the second table
    for i in range(len(top_10_assistants)):
        for j in range(len(top_10_assistants.columns)):
            table1[(i + 1, j)].set_facecolor(row_colors[i % 2])

    # Adjust the layout
    plt.tight_layout()
    plt.show()



def plot_player_stats(chosen_player, num_games, wins, draws, losses, points, efficiency, participations, goals_scored, assists):
    # Create a blank image
    width, height = 800, 300
    image = Image.new("RGB", (width, height), "#DDB06D")
    draw = ImageDraw.Draw(image)

    # Use Arial Bold font
    font_size = 22
    font_path_bold = "C:/Windows/Fonts/arialbd.ttf"  # Path to Arial Bold font on Windows
    font_bold = ImageFont.truetype(font_path_bold, font_size)

    # Define column width
    column_width = width // 2

    # First column (player)
    text_player = f"{chosen_player}"
    text_bbox_player = draw.textbbox((0, 0), text_player, font=font_bold)
    text_width_player = text_bbox_player[2] - text_bbox_player[0]
    text_height_player = text_bbox_player[3] - text_bbox_player[1]
    x_player = (column_width - text_width_player) / 5
    y_player = (height - text_height_player) / 2
    draw.text((x_player, y_player), text_player, font=ImageFont.truetype(font_path_bold, 30), fill=color_points_bg )

    # Second column (additional information)
    column2_x = column_width - 51  # Adjust to the right to separate columns
    column2_y = y_player - y_player/1.4 # Maintain the same initial height as the first column

    # Line 1: Number of Games
    text_games = f"{num_games} Games"
    text_bbox_games = draw.textbbox((0, 0), text_games, font=font_bold)
    text_width_games = text_bbox_games[2] - text_bbox_games[0]
    x_games = column2_x + (column_width - text_width_games) / 2.7
    draw.text((x_games, column2_y), text_games, font=ImageFont.truetype(font_path_bold, 30), fill=color_points_bg )

    # Line 2: Wins, Losses, and Draws
    text_results = f"Wins: {wins} | Draws: {draws} | Losses: {losses}"
    column2_y += text_height_player + 17  # Adjust down for the next line
    draw.text((column2_x, column2_y), text_results, font=font_bold, fill="#613A13")

    # Line 3: Points
    text_points = f"{points} Points"
    text_bbox_points = draw.textbbox((0, 0), text_points, font=ImageFont.truetype(font_path_bold, 30))
    text_width_points = text_bbox_points[2] - text_bbox_points[0]
    x_points = column2_x + (column_width - text_width_points) / 2.3
    column2_y += text_height_player + 30  # Adjust down for the next line
    draw.text((x_points, column2_y), text_points, font=ImageFont.truetype(font_path_bold, 30), fill="#00361e")

    # Line 4: Efficiency
    text_efficiency = f"{efficiency} Efficiency"
    text_bbox_efficiency = draw.textbbox((0, 0), text_efficiency, font=font_bold)
    text_width_efficiency = text_bbox_efficiency[2] - text_bbox_efficiency[0]
    x_efficiency = column2_x + (column_width - text_width_efficiency) / 2.7
    column2_y += text_height_player + 17  # Adjust down for the next line
    draw.text((x_efficiency, column2_y), text_efficiency, font=font_bold, fill="#1a915d")

    # Line 5: Participations
    text_participations = f"{participations} Goal Participations"
    text_bbox_participations = draw.textbbox((0, 0), text_participations, font=font_bold)
    text_width_participations = text_bbox_participations[2] - text_bbox_participations[0]
    x_participations = column2_x + (column_width - text_width_participations) / 5
    column2_y += text_height_player + 30  # Adjust down for the next line
    draw.text((x_participations, column2_y), text_participations, font=ImageFont.truetype(font_path_bold, 27), fill="#740013")

    # Line 6: Goals and Assists
    text_goals_assists = f"Goals: {goals_scored} | Assists: {assists}"
    text_bbox_goals_assists = draw.textbbox((0, 0), text_goals_assists, font=font_bold)
    text_width_goals_assists = text_bbox_goals_assists[2] - text_bbox_goals_assists[0]
    x_goals_assists = column2_x + (column_width - text_width_goals_assists) / 2.7
    column2_y += text_height_player + 17  # Adjust down for the next line
    draw.text((x_goals_assists, column2_y), text_goals_assists, font=font_bold, fill="#fe2713")

    # Display the image in Jupyter Notebook
    display(image)



def plot_player_classification(df_player_adjacent_points, chosen_player):
    # Create a figure and axes for the subplots
    fig, axs = plt.subplots(1, 1, figsize=(8, 4))  # Use only 1 subplot

    # Disable the axes
    axs.axis('off')

    # Table 1
    table1 = axs.table(cellText=df_player_adjacent_points.values, colLabels=df_player_adjacent_points.columns, cellLoc='center', loc='upper center')
    table1.auto_set_font_size(False)
    table1.set_fontsize(20)
    table1.scale(3.4, 3.4)  # Adjust the scale

    # Alternate row colors for better visualization
    for i in range(1, len(df_player_adjacent_points)+1):
        for j in range(len(df_player_adjacent_points.columns)):
            table1[(i, j)].set_facecolor(row_colors[(i-1) % 2])

    # Highlight the first row with a different color
    for i in range(len(df_player_adjacent_points.columns)):
        table1[(0, i)].set_facecolor(color_points_bg) 
        table1[(0, i)].get_text().set_color(color_points_lt)

    # Mark the player's row in light green
    for i in range(len(df_player_adjacent_points)):
        if df_player_adjacent_points.iloc[i]['Player'] == chosen_player:
            for j in range(len(df_player_adjacent_points.columns)):
                table1[(i+1, j)].set_facecolor('lightgreen')  # Light green color
            break


    # Make the sixth column bold
    for i in range(len(df_player_adjacent_points)):
        table1[(i+1, 6)].get_text().set_weight('bold')

    # Adjust margins manually
    plt.subplots_adjust(wspace=2.45)  # Adjust the space between subplots

    # Display the table
    plt.show()



def plot_player_goals_assits_classification(df_player_adjacent_scorers, df_player_adjacent_assists, chosen_player):
    # Create a figure and axes for the subplots
    fig, axs = plt.subplots(1, 2, figsize=(15, 5))

    # Disable the axes in both subplots
    for ax in axs:
        ax.axis('off')

    # Table 1: Scorers
    table1 = axs[0].table(cellText=df_player_adjacent_scorers.values, colLabels=df_player_adjacent_scorers.columns, cellLoc='center', loc='upper center')
    table1.auto_set_font_size(False)
    table1.set_fontsize(15)
    table1.scale(3.4, 3.4)  # Adjust the scale

    # Highlight the first row with a different color
    for i in range(len(df_player_adjacent_scorers.columns)):
        table1[(0, i)].set_facecolor(color_gols_bg)
        table1[(0, i)].get_text().set_color(color_gols_lt)

    # Alternate row colors for better visualization
    for i in range(1, len(df_player_adjacent_scorers)+1):
        for j in range(len(df_player_adjacent_scorers.columns)):
            table1[(i, j)].set_facecolor(row_colors[(i-1) % 2])

    # Mark the player's row in light green
    for i in range(len(df_player_adjacent_scorers)):
        if df_player_adjacent_scorers.iloc[i]['Player'] == chosen_player:
            for j in range(len(df_player_adjacent_scorers.columns)):
                table1[(i+1, j)].set_facecolor('lightgreen')  # Light green color
            break

    # Make the fourth column bold (index 3)
    for i in range(len(df_player_adjacent_scorers)):
        table1[(i + 1, 3)].get_text().set_weight('bold')

    # Set the title for the first table
    axs[0].set_title('Scorers Around Player', fontsize=16, fontweight='bold')

    # Table 2: Assists
    table2 = axs[1].table(cellText=df_player_adjacent_assists.values, colLabels=df_player_adjacent_assists.columns, cellLoc='center', loc='upper center')
    table2.auto_set_font_size(False)
    table2.set_fontsize(15)
    table2.scale(3.4, 3.4)  # Adjust the scale

    # Highlight the first row with a different color
    for i in range(len(df_player_adjacent_assists.columns)):
        table2[(0, i)].set_facecolor(color_assits_bg)
        table2[(0, i)].get_text().set_color(color_assits_lt)

    # Alternate row colors for better visualization
    for i in range(1, len(df_player_adjacent_assists)+1):
        for j in range(len(df_player_adjacent_assists.columns)):
            table2[(i, j)].set_facecolor(row_colors[(i-1) % 2])

    # Mark the player's row in light green
    for i in range(len(df_player_adjacent_assists)):
        if df_player_adjacent_assists.iloc[i]['Player'] == chosen_player:
            for j in range(len(df_player_adjacent_assists.columns)):
                table2[(i+1, j)].set_facecolor('lightgreen')  # Light green color
            break

    # Make the fourth column bold (index 3)
    for i in range(len(df_player_adjacent_assists)):
        table2[(i+1, 3)].get_text().set_weight('bold')

    # Set the title for the second table
    axs[1].set_title('Assists Around Player', fontsize=16, fontweight='bold')

    # Adjust margins manually
    plt.subplots_adjust(wspace=2.45)  # Adjust the space between subplots

    # Display the tables side by side
    plt.show()



def plot_player_best_performance(top_5_scorer_games, top_5_assist_games, chosen_player, has_goals, has_assists):
   # Check the conditions and plot the corresponding tables
    if has_goals and has_assists:
        # Create a 1x2 grid for accommodating the 2 tables
        gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1])

        # Create a figure with the grid
        fig = plt.figure(figsize=(15, 4.3))

        # Add the first table to the first subplot
        ax0 = plt.subplot(gs[0])
        ax0.axis('off')
        table0 = ax0.table(cellText=top_5_scorer_games.values, colLabels=top_5_scorer_games.columns, loc='center', cellLoc='center', colColours=[color_gols_bg ]*len(top_5_scorer_games.columns))
        table0.auto_set_font_size(False)
        table0.set_fontsize(15)
        table0.auto_set_column_width(col=list(range(len(top_5_scorer_games.columns))))
        table0.scale(2, 2.2)  # Adjust the value as needed
        ax0.text(0.5, 0.90, f'Top Number of Goals in a Match', fontsize=20, ha='center', va='center', color=color_gols_bg, fontweight='bold', transform=ax0.transAxes)

        # Add alternate row colors
        for i in range(1, len(top_5_scorer_games)+1):
            for j in range(len(top_5_scorer_games.columns)):
                table0[(i, j)].set_facecolor(row_colors[(i-1) % 2])

        # Set the color of the first row text
        for i in range(len(top_5_scorer_games.columns)):
            table0[(0, i)].get_text().set_color(color_gols_lt)

        # Add the second table to the second subplot
        ax1 = plt.subplot(gs[1])
        ax1.axis('off')
        table1 = ax1.table(cellText=top_5_assist_games.values, colLabels=top_5_assist_games.columns, loc='center', cellLoc='center', colColours=[color_assits_bg ]*len(top_5_assist_games.columns))
        table1.auto_set_font_size(False)
        table1.set_fontsize(15)
        table1.auto_set_column_width(col=list(range(len(top_5_assist_games.columns))))
        table1.scale(2, 2.2)  # Adjust the value as needed
        ax1.text(0.5, 0.90, f'Top Number of Assists in a Match', fontsize=20, ha='center', va='center', color=color_assits_bg, fontweight='bold', transform=ax1.transAxes)

        # Add alternate row colors
        for i in range(1, len(top_5_assist_games)+1):
            for j in range(len(top_5_assist_games.columns)):
                table1[(i, j)].set_facecolor(row_colors[(i-1) % 2])

        # Set the color of the first row text
        for i in range(len(top_5_assist_games.columns)):
            table1[(0, i)].get_text().set_color(color_assits_lt)

        # Adjust layout
        plt.tight_layout()

        # Display the tables together
        plt.show()
    elif has_goals:
        # If the player has only goals, plot the goals table
        plt.figure(figsize=(15, 5))
        plt.axis('off')
        table0 = plt.table(cellText=top_5_scorer_games.values, colLabels=top_5_scorer_games.columns, loc='center', cellLoc='center', colColours=[color_gols_bg ]*len(top_5_scorer_games.columns))
        table0.auto_set_font_size(False)
        table0.set_fontsize(15)
        table0.auto_set_column_width(col=list(range(len(top_5_scorer_games.columns))))
        table0.scale(2, 2.2)  # Adjust the value as needed
        plt.text(0.5, 0.90, f'Top Number of Goals in a Match', fontsize=20, ha='center', va='center', color=color_gols_bg, fontweight='bold', transform=plt.gca().transAxes)

        # Add alternate row colors
        for i in range(1, len(top_5_scorer_games)+1):
            for j in range(len(top_5_scorer_games.columns)):
                table0[(i, j)].set_facecolor(row_colors[(i-1) % 2])

        # Set the color of the first row text
        for i in range(len(top_5_scorer_games.columns)):
            table0[(0, i)].get_text().set_color(color_gols_lt)

        plt.tight_layout()
        plt.show()
    elif has_assists:
        # If the player has only assists, plot the assists table
        plt.figure(figsize=(15, 5))
        plt.axis('off')
        table1 = plt.table(cellText=top_5_assist_games.values, colLabels=top_5_assist_games.columns, loc='center', cellLoc='center', colColours=[color_assits_bg ]*len(top_5_assist_games.columns))
        table1.auto_set_font_size(False)
        table1.set_fontsize(25)
        table1.auto_set_column_width(col=list(range(len(top_5_assist_games.columns))))
        table1.scale(2, 2.2)  # Adjust the value as needed
        plt.text(0.5, 0.90, f'Top Number of Assists in a Match', fontsize=20, ha='center', va='center', color=color_assits_bg, fontweight='bold', transform=plt.gca().transAxes)

        # Add alternate row colors
        for i in range(1, len(top_5_assist_games)+1):
            for j in range(len(top_5_assist_games.columns)):
                table1[(i, j)].set_facecolor(row_colors[(i-1) % 2])

        # Set the color of the first row text
        for i in range(len(top_5_assist_games.columns)):
            table1[(0, i)].get_text().set_color(color_assits_lt)

        plt.tight_layout()
        plt.show()
    else:
        # If the player has neither goals nor assists, print a message
        print(f"The player {chosen_player} did not score any goals or assists.") 



def plot_frequent_teamates(players_count, chosen_player, max_value):
    # Adjust the figure size
    plt.figure(figsize=(12, 6))

    # Create the bar chart
    bars = players_count.plot(kind='bar', color=color_points_bg )

    # Add labels and title
    plt.ylabel('Number of Matches')
    plt.title(f'Most Frequent Teammates of {chosen_player}', fontsize=20, weight='bold')

    # Add values above the bars
    for bar in bars.patches:
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + max_value / 90, f'{int(bar.get_height())}', 
                 ha='center', va='bottom', color='black', weight='bold')

    # Remove borders
    sns.despine(left=True, right=True, top=True, bottom=False)    

    # Remove the x-axis legend
    plt.yticks([])

    # Remove background grid lines
    plt.grid(False)

    # Set the y-axis limit to max_value + 10% of it
    plt.ylim(0, max_value + 0.1 * max_value)

    plt.show()



def plot_win_lose_teamate(players, losses, draws, wins, games, efficiency, max_games, chosen_player):
    # Plotting the chart
    # Set the figure size
    plt.figure(figsize=(25, 12))

    # Bar width
    width = 0.87

    plt.bar(players, losses, label='Losses', color='#C00000', width=width)
    plt.bar(players, draws, label='Draws', bottom=losses, color='#7F7F7F', width=width)
    plt.bar(players, wins, label='Wins', bottom=[sum(x) for x in zip(losses, draws)], color='#548235', width=width)

    for i in range(len(players)):
        if losses[i] != 0:
            plt.text(players[i], losses[i] / 2, str(losses[i]), ha='center', va='center', color='white', fontsize=13, weight='bold')
        if draws[i] != 0:
            plt.text(players[i], losses[i] + draws[i] / 2, str(draws[i]), ha='center', va='center', color='yellow', fontsize=13, weight='bold')
        if wins[i] != 0:
            plt.text(players[i], losses[i] + draws[i] + wins[i] / 2, str(wins[i]), ha='center', va='center', color='white', fontsize=13, weight='bold')
        plt.text(players[i], losses[i] + draws[i] + wins[i] + max_games / 60, str(games[i]), ha='center', va='center', color='black', fontsize=13, weight='bold')
        plt.text(players[i], losses[i] + draws[i] + wins[i] + max_games / 25, str(efficiency[i]), ha='center', va='center', color='#100A49', fontsize=10, weight='bold', rotation=0) 

    # Set x-axis label rotation
    plt.xticks(rotation=60, weight='bold')        
    plt.title(f'Sum of Wins, Losses, Draws, and Efficiency by Teammate - {chosen_player}', fontsize=24, weight='bold')
    plt.legend()

    # Remove borders
    sns.despine(left=True, right=True, top=True, bottom=False)    

    # Remove the x-axis legend 
    plt.yticks([])  

    # Remove background grid lines
    plt.grid(False)

    # Set the y-axis limit to max_games + 10% of it
    plt.ylim(0, max_games + 0.1 * max_games)

    plt.show()



def plot_player_involvement(df_scorer_counts, df_assistant_counts, total_counts, percentage_assistant, percentage_scorer, chosen_player):
    # Adjust the figure size
    plt.figure(figsize=(6, 10))

    x = ['Direct Involvement']
    y1 = df_scorer_counts
    y2 = df_assistant_counts

    # Create the bars
    bar1 = plt.bar(x, y1, color=color_gols_bg, width=0.9)
    bar2 = plt.bar(x, y2, bottom=y1, color=color_assits_bg , width=0.9)

    # Add values and percentages above each bar
    for bar, value, percentage in zip(bar1, [y2], [percentage_assistant]):
        if value != 0:  # Check if the number of assists is different from 0
            plt.text(bar.get_x() + bar.get_width() / 1.5 - 0.15, total_counts - df_assistant_counts / 2,
                     f"{value} Assists ({percentage:.2f}%)", ha='center', va='bottom', color='black', weight='bold', size=12)

    for bar, value, percentage in zip(bar2, [y1], [percentage_scorer]):
        if value != 0:  # Check if the number of goals is different from 0
            plt.text(bar.get_x() + bar.get_width() / 1.5 - 0.15, (total_counts - df_assistant_counts) / 2,
                     f"{value} Goals ({percentage:.2f}%)", ha='center', va='bottom', color='black', weight='bold', size=12)

    # Add the total value at the top of the chart
    plt.text(bar1[0].get_x() + bar1[0].get_width() / 2, (y1 + y2),
             f"Total: {total_counts} Direct Involvement", ha='center', va='bottom', color='black', weight='bold', size=12)

    plt.legend(["Goals", "Assists"])
    plt.title("Direct Involvement in Goals (Goals + Assists) - {}".format(chosen_player), fontsize=16, weight='bold')

    # Remove borders
    sns.despine(left=True, right=True, top=True, bottom=False)

    # Remove background grid lines
    plt.grid(False)

    # Remove the x-axis legend
    plt.yticks([])
    plt.ylim(0, total_counts + total_counts * 0.15)
    plt.show()



def plot_player_involvement_period(part_counts, part_counts_goals, part_counts_assists, chosen_player, points_mapping):
    # Adjust the figure size
    plt.figure(figsize=(12, 6))

    wid = 0.2

    # Plot the bar chart
    bars = plt.bar(part_counts.index - 0.2, part_counts.values, color=[color_points_bg, color_points_bg, color_points_bg], width=wid)

    # Shift to the left for bar 2
    bars2 = plt.bar(part_counts_goals.index, part_counts_goals.values, color=[color_gols_bg, color_gols_bg, color_gols_bg], width=wid)

    # Shift to the right for bar 3
    bars3 = plt.bar(part_counts_assists.index + 0.2, part_counts_assists.values, color=[color_assits_bg, color_assits_bg, color_assits_bg], width=wid)

    # Title
    plt.title('Involvement according to game period - {}'.format(chosen_player), fontsize=20, weight='bold')

    # Add numbers on top of each bar
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, round(yval, 1),
                 ha='center', va='bottom', fontsize=15, weight='bold')

    # Add numbers on top of each bar
    for bar in bars2:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, round(yval, 1),
                 ha='center', va='bottom', fontsize=15, weight='bold')

    # Add numbers on top of each bar
    for bar in bars3:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, round(yval, 1),
                 ha='center', va='bottom', fontsize=15, weight='bold')

    # Remove borders
    sns.despine(left=True, right=True, top=True, bottom=False)

    # Remove the y-axis legend
    plt.yticks([])

    # Modify x-axis ticks
    plt.xticks(list(points_mapping.values()), list(points_mapping.keys()), fontweight='bold', fontsize=15)

    # Remove background grid lines
    plt.grid(False)

    # Legend
    plt.legend(["Involvement", "Goals", "Assists"])

    plt.show()




def plot_player_involviment_type(part_counts, part_counts_goals, part_counts_assists, chosen_player, points_mapping):
    # Adjust the figure size
    plt.figure(figsize=(12, 6))

    wid = 0.2

    # Plot the bar chart
    bars = plt.bar(part_counts.index - 0.2, part_counts.values, color=[color_points_bg , color_points_bg , color_points_bg ], width=wid)

    # Shift to the left for bar 2
    bars2 = plt.bar(part_counts_goals.index, part_counts_goals.values, color=[color_gols_bg, color_gols_bg, color_gols_bg], width=wid)

    # Shift to the right for bar 3
    bars3 = plt.bar(part_counts_assists.index + 0.2, part_counts_assists.values, color=[color_assits_bg , color_assits_bg , color_assits_bg ], width=wid)

    # Title
    plt.title('Involvement in Goal Types - {}'.format(chosen_player), fontsize=20, weight='bold')

    # Add numbers on top of each bar
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, round(yval, 1),
                 ha='center', va='bottom', fontsize=15, weight='bold')

    # Add numbers on top of each bar
    for bar in bars2:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, round(yval, 1),
                 ha='center', va='bottom', fontsize=15, weight='bold')

    # Add numbers on top of each bar
    for bar in bars3:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, round(yval, 1),
                 ha='center', va='bottom', fontsize=15, weight='bold')

    # Remove borders
    sns.despine(left=True, right=True, top=True, bottom=False)

    # Remove the y-axis legend
    plt.yticks([])

    # Modify x-axis ticks
    plt.xticks(list(points_mapping.values()), list(points_mapping.keys()), fontweight='bold', fontsize=15)

    # Remove background grid lines
    plt.grid(False)

    # Legend
    plt.legend(["Involvement", "Goals", "Assists"])

    plt.show()




def plot_player_assists_teamates(assistant_counts_scorer, no_assistant_counts, assistant_counts_assistant, chosen_player):
    # Find the highest number in the two datasets
    max_value_scorer = assistant_counts_scorer.max()
    max_value_no_assist = no_assistant_counts.max()
    max_value_assistant = assistant_counts_assistant.max()

    # Number of bars to define 'width_ratios': [1, 0.05, 1]'
    num_g1 = assistant_counts_scorer.count()
    num_g3 = assistant_counts_assistant.count()
    g_max = max(num_g1, num_g3)  # Find the highest value

    # Logic to define the width
    if g_max > 19:
        width = 0.04
    elif g_max > 12:
        width = 0.05    
    elif g_max > 8:
        width = 0.1
    elif g_max > 4:
        width = 0.2
    elif g_max > 2:
        width = 0.25    
    else:
        width = 0.3

    # Find the highest number among the two datasets
    max_value_total = max(max_value_scorer, max_value_assistant, max_value_no_assist)
    # Check conditions to decide which charts to plot
    if assistant_counts_scorer.empty and no_assistant_counts.empty and assistant_counts_assistant.empty:
        # Do not plot any charts, as they are all empty
        print('No charts to plot')

    elif not assistant_counts_scorer.empty and not no_assistant_counts.empty and not assistant_counts_assistant.empty:
        # Adjust figure size and create subplots
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 6), gridspec_kw={'width_ratios': [1, width, 1]})

        # First chart
        bars1 = assistant_counts_scorer.plot(kind='bar', color=color_gols_bg , ax=ax1)
        ax1.set_title('Received Assists', fontsize=16, fontweight='bold', color=color_gols_bg , fontfamily='arial')
        for bar in bars1.patches:
            ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05, f'{int(bar.get_height())}', 
                     ha='center', va='bottom', color='black', weight='bold')
        ax1.spines['right'].set_visible(False)  # Remove right border
        ax1.spines['left'].set_visible(False)   # Remove left border
        ax1.spines['top'].set_visible(False)    # Remove top border
        ax1.invert_xaxis()  # Invert the order of bars on the x-axis
        ax1.set_yticks([])  # Remove y-axis labels
        ax1.grid(False)  # Remove grid lines

        # Second chart
        bars2 = no_assistant_counts.plot(kind='bar', color=color_points_bg , ax=ax2, width=0.7)
        ax2.set_title('Player: {}'.format(chosen_player), fontsize=18, fontweight='bold', color=color_points_bg , fontfamily='arial')
        ax2.set_yticks([])  # Remove y-axis labels
        for bar in bars2.patches:
            ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05, f'{int(bar.get_height())}', 
                     ha='center', va='bottom', color='black', weight='bold')  
        ax2.spines['left'].set_visible(False)   # Remove left border
        ax2.spines['right'].set_visible(False)  # Remove right border
        ax2.spines['top'].set_visible(False)    # Remove top border
        ax2.set_xticklabels(['No Assistance'], rotation=90, ha='center') # Set x-axis labels
        ax2.grid(False)  # Remove grid lines

        # Third chart
        bars3 = assistant_counts_assistant.plot(kind='bar', color=color_assits_bg , ax=ax3)
        ax3.set_title('Granted Assists', fontsize=16, fontweight='bold', color=color_assits_bg , fontfamily='arial')
        ax3.set_yticks([])  # Remove y-axis labels
        for bar in bars3.patches:
            ax3.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05, f'{int(bar.get_height())}', 
                     ha='center', va='bottom', color='black', weight='bold')
        ax3.spines['left'].set_visible(False)   # Remove left border
        ax3.spines['right'].set_visible(False)  # Remove right border
        ax3.spines['top'].set_visible(False)    # Remove top border
        ax3.grid(False)  # Remove grid lines

        # Set y-axis to include the highest value
        y_max = max(max_value_scorer, max_value_assistant, max_value_no_assist)
        ax1.set_ylim(0, y_max + 1.5)
        ax2.set_ylim(0, y_max + 1.5)
        ax3.set_ylim(0, y_max + 1.5)

        # Adjust layout to avoid overlap
        plt.tight_layout()

        # Show the charts
        plt.show()   

    elif assistant_counts_scorer.empty and not no_assistant_counts.empty and assistant_counts_assistant.empty:
        # Plot only the second chart
        fig, ax2 = plt.subplots(figsize=(10, 6))

        # Second chart
        bars2 = no_assistant_counts.plot(kind='bar', color=color_points_bg , ax=ax2, width=0.7)
        ax2.set_title('Player: {}'.format(chosen_player), fontsize=18, fontweight='bold', color=color_points_bg , fontfamily='arial')
        ax2.set_yticks([])  # Remove y-axis labels
        for bar in bars2.patches:
            ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05, f'{int(bar.get_height())}', 
                     ha='center', va='bottom', color='black', weight='bold')  
        ax2.spines['left'].set_visible(False)   # Remove left border
        ax2.spines['right'].set_visible(False)  # Remove right border
        ax2.spines['top'].set_visible(False)    # Remove top border
        ax2.set_xticklabels(['No Assistance'], rotation=90, ha='center') # Set x-axis labels
        ax2.grid(False)  # Remove grid lines

        # Set y-axis to include the highest value
        y_max = max_value_no_assist
        ax2.set_ylim(0, y_max + 1.5)

        # Adjust layout to avoid overlap
        plt.tight_layout()

        # Show the chart
        plt.show()   

    elif not assistant_counts_scorer.empty and no_assistant_counts.empty and assistant_counts_assistant.empty:
        # Plot only the first chart
        fig, ax1 = plt.subplots(figsize=(10, 6))

        # First chart
        bars1 = assistant_counts_scorer.plot(kind='bar', color=color_gols_bg , ax=ax1)
        ax1.set_title('Received Assists', fontsize=16, fontweight='bold', color=color_gols_bg , fontfamily='arial')
        for bar in bars1.patches:
            ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05, f'{int(bar.get_height())}', 
                     ha='center', va='bottom', color='black', weight='bold')
        ax1.spines['right'].set_visible(False)  # Remove right border
        ax1.spines['left'].set_visible(False)   # Remove left border
        ax1.spines['top'].set_visible(False)    # Remove top border
        ax1.invert_xaxis()  # Invert the order of bars on the x-axis
        ax1.set_yticks([])  # Remove y-axis labels
        ax1.grid(False)  # Remove grid lines

        # Set y-axis to include the highest value
        y_max = max_value_scorer
        ax1.set_ylim(0, y_max + 1.5)

        # Adjust layout to avoid overlap
        plt.tight_layout()

        # Show the chart
        plt.show()      

    elif assistant_counts_scorer.empty and no_assistant_counts.empty and not assistant_counts_assistant.empty:
        # Plot only the third chart
        fig, ax3 = plt.subplots(figsize=(10, 6))

        # Third chart
        bars3 = assistant_counts_assistant.plot(kind='bar', color=color_assits_bg , ax=ax3)
        ax3.set_title('Granted Assists', fontsize=16, fontweight='bold', color=color_assits_bg , fontfamily='arial')
        ax3.set_yticks([])  # Remove y-axis labels
        for bar in bars3.patches:
            ax3.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05, f'{int(bar.get_height())}', 
                     ha='center', va='bottom', color='black', weight='bold')
        ax3.spines['left'].set_visible(False)   # Remove left border
        ax3.spines['right'].set_visible(False)  # Remove right border
        ax3.spines['top'].set_visible(False)    # Remove top border
        ax3.grid(False)  # Remove grid lines

        # Set y-axis to include the highest value
        y_max = max_value_assistant
        ax3.set_ylim(0, y_max + 1.5)

        # Adjust layout to avoid overlap
        plt.tight_layout()

        # Show the chart
        plt.show()	
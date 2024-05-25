import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_rewards(base_file_name, save_path=None):
    # Create unique file names for each type of reward
    filenames = ['goal_reward_', 'timeout_penalty_', 'wall_penalty_', 'obs_penalty_', 'total_reward_','total_successes_']

     # Read existing data from the CSV files if they exist
    total_reward_data = pd.DataFrame()
    goal_reward_data = pd.DataFrame()
    wall_penalty_data = pd.DataFrame()
    obs_penalty_data = pd.DataFrame()
    timeout_penalty_data = pd.DataFrame()
    successes = pd.DataFrame()

    for i in range(1):
        goal_reward_data = pd.concat([goal_reward_data,pd.read_csv(f'{base_file_name}{filenames[0]}{i}.csv')], ignore_index=True)
        wall_penalty_data = pd.concat([wall_penalty_data,pd.read_csv(f'{base_file_name}{filenames[2]}{i}.csv')], ignore_index=True)
        obs_penalty_data = pd.concat([obs_penalty_data,pd.read_csv(f'{base_file_name}{filenames[2]}{i}.csv')], ignore_index=True)
        timeout_penalty_data = pd.concat([timeout_penalty_data,pd.read_csv(f'{base_file_name}{filenames[1]}{i}.csv')], ignore_index=True)
        total_reward_data = pd.concat([total_reward_data,pd.read_csv(f'{base_file_name}{filenames[3]}{i}.csv')], ignore_index=True)
        successes = pd.concat([successes,pd.read_csv(f'{base_file_name}{filenames[4]}{i}.csv')], ignore_index=True)

    import numpy as np
    total_reward_data = total_reward_data.sum(axis=1)
    goal_reward_data = goal_reward_data.sum(axis=1)
    wall_penalty_data = wall_penalty_data.sum(axis=1)
    obs_penalty_data = obs_penalty_data.sum(axis=1)
    timeout_penalty_data = timeout_penalty_data.sum(axis=1)
    total_successes = successes.sum(axis=1)

    # Plot and save each reward type individually
    save_plots = []

    plt.figure(figsize=(10, 6))
    plt.plot(total_reward_data, color='black')
    plt.title('Total Reward')
    plt.xlabel('Time Step')
    plt.ylabel('Reward')
    if save_path:
        save_path_total = os.path.join(save_path, 'total_reward_plot.png')
        plt.savefig(save_path_total)
        save_plots.append(save_path_total)
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(goal_reward_data, color='green')
    plt.title('Goal Reward')
    plt.xlabel('Time Step')
    plt.ylabel('Reward')
    if save_path:
        save_path_goal = os.path.join(save_path, 'goal_reward_plot.png')
        plt.savefig(save_path_goal)
        save_plots.append(save_path_goal)
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(wall_penalty_data, color='red')
    plt.title('Wall Penalty')
    plt.xlabel('Time Step')
    plt.ylabel('Penalty')
    if save_path:
        save_path_wall = os.path.join(save_path, 'wall_penalty_plot.png')
        plt.savefig(save_path_wall)
        save_plots.append(save_path_wall)
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(obs_penalty_data, color='red')
    plt.title('Obstacle Penalty')
    plt.xlabel('Time Step')
    plt.ylabel('Penalty')
    if save_path:
        save_path_obs = os.path.join(save_path, 'obs_penalty_plot.png')
        plt.savefig(save_path_obs)
        save_plots.append(save_path_obs)
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(timeout_penalty_data, color='red')
    plt.title('Timeout Penalty')
    plt.xlabel('No. of timeouts')
    plt.ylabel('Penalty')
    if save_path:
        save_path_timeout = os.path.join(save_path, 'timeout_penalty_plot.png')
        plt.savefig(save_path_timeout)
        save_plots.append(save_path_timeout)
    plt.show()

    # print("Success Rate:",successes)

    return save_plots

# Example usage with saving to a specific path
save_paths = plot_rewards("/common/home/hk919/walk-these-ways/rewards/", save_path="/common/home/hk919/walk-these-ways/imdump/")

# save_paths will contain the paths to the saved plots if save_path is provided
print("Saved plots:", save_paths)

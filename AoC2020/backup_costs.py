import subprocess
import shlex
import json
from money import Money

doctl_binary = "/usr/local/bin/doctl"


def init():

    # get snapshot data as json
    print("fetch snapshot data from digitalocean")
    doctl_response = doctl(f"{doctl_binary} compute snapshot list --output json")
    snapshot_data = json.loads(doctl_response.stdout.decode("utf-8"))

    return snapshot_data


def doctl(command: str):
    return subprocess.run(
        shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )


def main():

    cost_per_gb_per_month = 0.05
    total_size = 0

    snapshot_data = init()
    for snapshot in snapshot_data:
        print(
            f'Snapshot {snapshot["name"]}: '
            + f'size {snapshot["size_gigabytes"]:.2f} GB, '
            + f'{Money(snapshot["size_gigabytes"]*cost_per_gb_per_month/30,"USD").format("de_DE")} per day, '
            + f'{Money(snapshot["size_gigabytes"]*cost_per_gb_per_month, "USD").format("de_DE")} per month, '
        )
        total_size += snapshot["size_gigabytes"]

    print(f"\nTotal: {total_size:.2f} GB")
    print(
        f"Total prize per day: {Money(total_size*cost_per_gb_per_month/30,'USD').format('de_DE')}"
    )
    print(f"Total prize per month: {total_size*cost_per_gb_per_month:,.2f} $")


if __name__ == "__main__":
    main()

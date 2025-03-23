import yt_dlp

link = input("Enter the link of the video you want to download: ")
save_path = input("Where would you like to save the video? ")

try:
    # Get video information
    ydl_opts = {'listformats': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(link, download=False)
    
    formats = info_dict.get('formats', [])

    # Print all available resolutions
    print("Available resolutions:")
    resolutions = []
    for f in formats:
        if f.get('height') is not None:
            res = f'{f["height"]}p'
            if res not in resolutions:
                resolutions.append(res)
                print(res)
    
    # Prompt user to select a resolution
    resolution = input("Enter the desired resolution: ")
    
    # Set download options with selected resolution
    ydl_opts = {
        'outtmpl': save_path + '/%(title)s.%(ext)s',
        'format': f'best[height={resolution[:-1]}]'
    }

    # Download the video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

    print("Download completed")
except Exception as e:
    print(f"An error occurred: {e}")

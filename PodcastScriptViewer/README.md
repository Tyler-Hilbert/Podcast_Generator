# Paragraph Summary Viewer
This website is a support tool that helps review generated podcast scripts by displaying each transcript paragraph next to its summary.

## Usage
1. Create a `.json` file with the fields `paragraph_transcript` and `paragraph_summary`.
2. Update the fetch path in `ParagraphSummaryViewer.html` (line 16).
3. Start a local server using Python:
   ```bash
   python3 -m http.server 8000
   ```
4. Open your browser and visit [http://localhost:8000/](http://localhost:8000/).
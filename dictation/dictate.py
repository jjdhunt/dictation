import typer
from dictation.dictation import dictate

app = typer.Typer()

@app.command()
def run():
    """Continuously check if Ctrl+Space is pressed or released and record audio accordingly."""
    print("Ready. Press and hold <ctrl>+<space> to dictate. The transcribed dictation will appear in your clipboard when completed.")
    dictate()
    
if __name__ == "__main__":
    app()
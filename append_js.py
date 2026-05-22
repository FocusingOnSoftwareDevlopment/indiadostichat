import sys

js_code = """
// --- 8. UNO Tournament Razorpay Integration ---
document.addEventListener('DOMContentLoaded', () => {
    const RAZORPAY_KEY_ID = "YOUR_RAZORPAY_KEY_ID";
    const GOOGLE_SCRIPT_URL = "YOUR_GOOGLE_APPS_SCRIPT_WEB_APP_URL";

    const form = document.getElementById("uno-form");
    const payButton = document.getElementById("pay-uno-btn");
    const message = document.getElementById("uno-message");

    if (payButton) {
        payButton.addEventListener("click", function () {
            const usernameInput = document.getElementById("uno-username");
            const emailInput = document.getElementById("uno-email");
            const notesInput = document.getElementById("uno-notes");
            
            const username = usernameInput ? usernameInput.value.trim() : "";
            const email = emailInput ? emailInput.value.trim() : "";
            const notes = notesInput ? notesInput.value.trim() : "";

            if (!username) {
                if (message) {
                    message.textContent = "Please enter your IndiaDostiChat username.";
                    message.className = "form-message error";
                }
                return;
            }

            if (message) {
                message.textContent = "Opening Razorpay payment...";
                message.className = "form-message info";
            }

            const options = {
                key: RAZORPAY_KEY_ID,
                amount: 2500,
                currency: "INR",
                name: "IndiaDostiChat",
                description: "DUNO Tournament Entry Fee",
                prefill: {
                    name: username,
                    email: email
                },
                notes: {
                    username: username,
                    tournament: "IndiaDostiChat DUNO Tournament"
                },
                handler: function (response) {
                    const payload = {
                        username: username,
                        email: email,
                        razorpay_payment_id: response.razorpay_payment_id,
                        payment_status: "Paid - Client Reported",
                        amount: "25",
                        tournament: "IndiaDostiChat DUNO Tournament",
                        notes: notes,
                        source: "duno-tournament"
                    };

                    fetch(GOOGLE_SCRIPT_URL, {
                        method: "POST",
                        mode: "no-cors",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify(payload)
                    }).catch(err => console.error("Form submission error", err));

                    if (message) {
                        message.textContent = "Payment successful. Registration submitted. Payment ID: " + response.razorpay_payment_id + ". Your payment will be manually verified before slot confirmation.";
                        message.className = "form-message success";
                    }

                    if (form) {
                        form.reset();
                    }
                },
                modal: {
                    ondismiss: function () {
                        if (message) {
                            message.textContent = "Payment was not completed.";
                            message.className = "form-message error";
                        }
                    }
                },
                theme: {
                    color: "#16a34a"
                }
            };

            if (typeof Razorpay !== 'undefined') {
                const rzp = new Razorpay(options);
                rzp.open();
            } else {
                if (message) {
                    message.textContent = "Razorpay script not loaded. Please refresh the page.";
                    message.className = "form-message error";
                }
            }
        });
    }
});
"""

with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    existing_content = f.read()

if "// --- 8. UNO Tournament Razorpay Integration ---" not in existing_content:
    with open('assets/js/main.js', 'a', encoding='utf-8') as f:
        f.write('\n' + js_code + '\n')
    print('Appended JS successfully.')
else:
    print('JS already appended, skipping append.')

import re

def minify_css(css):
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
    css = re.sub(r'\s+', ' ', css)
    css = re.sub(r'\s*([{}:;,>+~])\s*', r'\1', css)
    css = css.replace(';}', '}')
    return css.strip()

def minify_js(js):
    pattern = re.compile(r'("(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\'|`(?:[^`\\]|\\.)*`|/\*[\s\S]*?\*/|//.*)')
    def replacer(match):
        s = match.group(0)
        if s.startswith('/*') or s.startswith('//'):
            return ''
        return s
    js = pattern.sub(replacer, js)
    js = re.sub(r'\s+', ' ', js)
    return js.strip()

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

with open('assets/css/style.min.css', 'w', encoding='utf-8') as f:
    f.write(minify_css(css_content))

with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

with open('assets/js/main.min.js', 'w', encoding='utf-8') as f:
    f.write(minify_js(js_content))

print('Minified successfully.')

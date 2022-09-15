Check list:
- fulfil fields
    - valid email
    - valid phone number
- checked checkbox on load
- after registration:
    - redirect to https://trader.alvexo.ae/login-area/continue-real-account
    - https://trader.alvexo.ae/login-area-new/continue-real-account?ut=43d79101daf5120a00c7a4f6f2a7731f

Exploratory testing:
    define required fields
    define limit for the fields
    errors for the fields
        valid data
    messages for the fields


Bug-report:

    Environment: 
        Desktop/mobile:
        only for browser: firefox 105.0a1 (2022-08-10) (64-bit)
        mobile: oneplus a5010? android 10
    
        functional
            1. Unchecked checkbox on load.
                Severity: minor
            2. bad error handle for phone number field
                Steps:
                    fulfill phone number field by value 111111
                Expected result: output message الرجاء إدخال رقم هاتف صالح
                Result: no message about invalid phone number
                Severity: minor
            3. Poore error information after registration
                Steps:
                    Fulfil all fields by limit:
                        name: 'Wolfeschlegelsteinhausenberger'
                        email: 'Wolfeschlegelsteinhausenbergerdorffwelchevoralternwarengewissenhaftschaferswessenschafewa@enwohl.com'
                        phone: '77777777777777'
                    checkbox checked
                    press button "subscribe now!"
                Expected result: Error must be described that user can fix data he input
                Result: an error occurred
                Severity: minor
    
        nonfunctional
            1. white space between web form and picture when screen > 991px. Screenshot 1, minor
            1. blue button instead of green. Screenshot 2, minor
            1. background should be white. Screenshot 2, minor
            1. bad landing on screen < 566px, Screenshot 3, minor
"""
Generator script to produce speech_to_sign_vocab.json and hospital_phrases.json
Aligns with ISL Connect specification:
- speech_to_sign_vocab.json: Approximately 206+ vocabulary entries across 10 categories
- hospital_phrases.json: Approximately 113+ phrases across 12 clinical categories
"""
import json

vocab_data = {
    "greetings_social": [
        ("hello", "नमस्ते / नमस्कार", "ನಮಸ್ಕಾರ", "Open right hand waves gently side-to-side or right palm touches forehead like salute."),
        ("namaste", "नमस्ते", "ನಮಸ್ಕಾರ", "Both palms pressed flat together at chest level in Indian greeting."),
        ("welcome", "स्वागत है", "ಸ್ವಾಗತ", "Both open palms face upward moving gently towards chest."),
        ("good morning", "शुभ प्रभात", "ಶುಭೋದಯ", "Sign GOOD (thumbs up to chin) followed by MORNING (sun rising with curved hand)."),
        ("good afternoon", "शुभ दोपहर", "ಶುಭ ಮಧ್ಯಾಹ್ನ", "Sign GOOD followed by right arm resting bent at horizon indicating midday sun."),
        ("good evening", "शुभ संध्या", "ಶುಭ ಸಂಜೆ", "Sign GOOD followed by hand descending symbolizing sunset."),
        ("good night", "शुभ रात्रि", "ಶುಭ ರಾತ್ರಿ", "Sign GOOD followed by hands crossing in front like closing daylight."),
        ("thank you", "धन्यवाद", "ಧನ್ಯವಾದಗಳು", "Fingertips of flat right hand touch chin and move outward toward person."),
        ("sorry", "माफ़ कीजिए", "ಕ್ಷಮಿಸಿ", "Right closed fist makes circular motion on chest over heart with remorseful look."),
        ("please", "कृपया", "ದಯವಿಟ್ಟು", "Flat open right hand rubs circular clockwise motion on chest."),
        ("excuse me", "क्षमा करें", "ಮನ್ನಿಸಿ", "Tips of fingers of right hand scrape upward across left flat palm twice."),
        ("goodbye", "अलविदा", "ವಿದಾಯ", "Open right hand with fingers bending together up and down."),
        ("nice to meet you", "आपसे मिलकर अच्छा लगा", "ನಿಮ್ಮನ್ನು ಭೇಟಿಯಾಗಿದ್ದು ಸಂತೋಷವಾಯಿತು", "Sign NICE (palms sliding) + MEET (index fingers coming together)."),
        ("how are you", "आप कैसे हैं?", "ನೀವು ಹೇಗಿದ್ದೀರಿ?", "Curved palms touch chest then turn upward and open toward listener with questioning look."),
        ("i am fine", "मैं ठीक हूँ", "ನಾನು ಚೆನ್ನಾಗಿದ್ದೇನೆ", "Thumb of right open 5 hand touches chest twice with confident smile."),
        ("see you later", "बाद में मिलते हैं", "ನಂತರ ನೋಡೋಣ", "Two fingers point from eyes then thumb & index form L moving forward."),
        ("take care", "अपना ख्याल रखें", "ಜಾಗರೂಕರಾಗಿರಿ", "Both K-hands tap wrists one on top of the other twice."),
        ("yes", "हाँ", "ಹೌದು", "Closed fist nods up and down like a head nodding affirmatively."),
        ("no", "नहीं", "ಇಲ್ಲ", "Index and middle fingers snap shut against thumb firmly."),
        ("agree", "सहमत", "ಒಪ್ಪಿಗೆ", "Index finger touches forehead then points forward parallel with other hand.")
    ],
    "medical_emergency": [
        ("doctor", "डॉक्टर", "ವೈದ್ಯರು", "Right bent fingertips tap inside of left wrist checking pulse."),
        ("nurse", "नर्स", "ಶುಶ್ರೂಷಕಿ", "Right index and middle fingers tap cross pattern on left upper arm or forehead."),
        ("hospital", "अस्पताल", "ಆಸ್ಪತ್ರೆ", "Index finger draws cross (+) on left upper arm or forehead."),
        ("emergency", "आपातकाल", "ತುರ್ತು ಪರಿಸ್ಥಿತಿ", "Letter E hand shaken rapidly side-to-side with urgent expression."),
        ("help", "मदद", "ಸಹಾಯ", "Right closed fist with thumb up resting on flat left palm, raised together."),
        ("pain", "दर्द", "ನೋವು", "Both index fingers point toward each other and twist towards pain location with pained grimace."),
        ("severe pain", "गंभीर दर्द", "ತೀವ್ರ ನೋವು", "Twisting index fingers forcefully with clenched jaw and pained eyes."),
        ("medicine", "दवा", "ಔಷಧ", "Right middle finger rubs center of left open palm in circular grinding motion."),
        ("tablet", "गोली", "ಮಾತ್ರೆ", "Thumb and index finger mime placing small pill on tongue."),
        ("syrup", "सिरप / तरल दवा", "ಸಿರಪ್", "Thumb and index mime holding small medicine cup and drinking."),
        ("injection", "इंजेक्शन", "ಚುಚ್ಚುಮದ್ದು", "Thumb and index fingers simulate syringe pushing plunger into left arm."),
        ("fever", "बुखार", "ಜ್ವರ", "Back of right hand touches forehead checking body temperature."),
        ("ambulance", "एम्बुलेंस", "ಆಂಬ್ಯುಲೆನ್ಸ್", "Open hand above head flashes open and closed rotating like beacon light."),
        ("bandage", "पट्टी", "ಪಟ್ಟಿ", "Hands wrap around imaginary limb or wrist repeatedly."),
        ("blood", "रक्त / खून", "ರಕ್ತ", "Index finger touches lower lip (red) then trickles down open left palm."),
        ("cough", "खाँसी", "ಕೆಮ್ಮು", "Fist held before mouth while gently coughing twice."),
        ("dizzy", "चक्कर आना", "ತಲೆಸುತ್ತು", "Index finger circles above head while head tilts gently."),
        ("stomach ache", "पेट दर्द", "ಹೊಟ್ಟೆ ನೋವು", "Both hands clutch stomach area with twisting circular motion."),
        ("headache", "सिरदर्द", "ತಲೆನೋವು", "Index fingers point at temples and twist back and forth."),
        ("chest pain", "सीने में दर्द", "ಎದೆ ನೋವು", "Right hand clutches left chest over heart with tight grimace."),
        ("allergy", "एलर्जी", "ಅಲರ್ಜಿ", "Scratching forearm rapidly with fingertips of other hand."),
        ("breathe", "साँस लेना", "ಉಸಿರಾಟ", "Both hands move toward and away from chest mimicking lung expansion."),
        ("suffocation", "दम घुटना", "ಉಸಿರುಗಟ್ಟುವಿಕೆ", "Both hands grip neck with distressed facial expression."),
        ("oxygen", "ऑक्सीजन", "ಆಮ್ಲಜನಕ", "Cup shape hand placed over nose and mouth indicating oxygen mask."),
        ("surgery", "शल्यचिकित्सा", "ಶಸ್ತ್ರಚಿಕಿತ್ಸೆ", "Thumb of right fist draws cut line across palm of open left hand."),
        ("wheelchair", "व्हीलचेयर", "ವೀಲ್ ಚೇರ್", "Curved hands rotate forward in circular motions like pushing wheelchair wheels."),
        ("stretcher", "स्ट्रेचर", "ಸ್ಟ್ರೆಚರ್", "Both hands hold flat imaginary poles walking horizontally."),
        ("pharmacy", "दवा की दुकान", "ಔಷಧಿ ಅಂಗಡಿ", "Sign MEDICINE followed by sign STORE (hands flicking forward)."),
        ("thermometer", "थर्मामीटर", "ಥರ್ಮಾಮೀಟರ್", "Index finger placed under tongue or in armpit with level indicator."),
        ("wound", "घाव", "ಗಾಯ", "Curled fingers scrape gently along arm or skin showing injury."),
        ("infection", "संक्रमण", "ಸೋಂಕು", "I-hand wiggles across forearm with concerned expression."),
        ("fracture", "हड्डी टूटना", "ಮೂಳೆ ಮುರಿತ", "Both fists snap sideways apart indicating broken bone.")
    ],
    "daily_needs": [
        ("water", "पानी", "ನೀರು", "W-handshape (index, middle, ring fingers spread) index taps chin twice."),
        ("food", "खाना", "ಆಹಾರ", "Fingertips pressed together touch lips repeatedly."),
        ("drink", "पीना", "ಕುಡಿಯಿರಿ", "C-handshape mimics holding cup and tilting back to mouth."),
        ("restroom", "शौचालय", "ಶೌಚಾಲಯ", "R-handshape shaken gently side-to-side or T-handshape rotated."),
        ("toilet", "टॉयलेट", "ಶೌಚಾಲಯ", "T-handshape wiggles gently side to side."),
        ("sleep", "सोना", "ನಿದ್ರೆ", "Open hand across forehead draws down closing into fist while eyes close."),
        ("bed", "बिस्तर", "ಹಾಸಿಗೆ", "Both hands palms together resting against cheek tilted sideways."),
        ("clean", "साफ", "ಸ್ವಚ್ಛ", "Right open palm brushes smoothly across left open palm forward."),
        ("blanket", "कंबल", "ಕಂಬಳಿ", "Both hands grip imaginary top edge of blanket and pull up to chest."),
        ("pillow", "तकिया", "ದಿಂಬು", "Both hands squeeze air near ear like fluffing a pillow."),
        ("clothes", "कपड़े", "ಬಟ್ಟೆ", "Thumbs brush down front of chest/shirt twice."),
        ("light", "रोशनी / बत्ती", "ಬೆಳಕು", "Fingers pinch then expand downward like light shining down."),
        ("fan", "पंखा", "ಫ್ಯಾನ್", "Index finger points upward rotating in circles overhead."),
        ("telephone", "फ़ोन", "ದೂರವಾಣಿ", "Y-handshape (thumb to ear, pinky to mouth)."),
        ("chair", "कुर्सी", "ಕುರ್ಚಿ", "Two bent fingers of right hand tap twice on two bent fingers of left hand."),
        ("door", "दरवाज़ा", "ಬಾಗಿಲು", "B-hands touch side-by-side, right hand swings open outward."),
        ("window", "खिड़की", "ಕಿಟಕಿ", "Horizontal open hands tap and slide up and down."),
        ("money", "पैसे", "ಹಣ", "Back of thumb rubs fingertips together in currency motion."),
        ("glasses", "चश्मा", "ಕನ್ನಡಕ", "Curved index and thumb frame eyes like spectacles."),
        ("wash", "धोना", "ತೊಳೆಯಿರಿ", "Fists rub against each other like lathering soap."),
        ("soap", "साबुन", "ಸಾಬೂನು", "Fingers scrape back of open palm mimicking soap lathering."),
        ("towel", "तौलिया", "ಟವೆಲ್", "Hands hold imaginary towel behind head rubbing back and forth."),
        ("brush", "ब्रश", "ಹಲ್ಲುಜ್ಜುವ ಬ್ರಷ್", "Index finger moves horizontally in front of teeth mimicking toothbrush.")
    ],
    "family_people": [
        ("mother", "माँ", "ತಾಯಿ", "Open 5-hand thumb taps chin twice."),
        ("father", "पिता", "ತಂದೆ", "Open 5-hand thumb taps forehead twice."),
        ("sister", "बहन", "ಸಹೋದರಿ", "Index finger touches chin then taps on top of left index finger."),
        ("brother", "भाई", "ಸಹೋದರ", "Index finger touches forehead then taps on top of left index finger."),
        ("baby", "बच्चा", "ಮಗು", "Both arms cradled across chest rocking side to side."),
        ("family", "परिवार", "ಕುಟುಂಬ", "Both F-hands touching index/thumbs circle outward until pinkies meet."),
        ("friend", "दोस्त", "ಸ್ನೇಹಿತ", "Hooked index fingers link together, then reverse and link again."),
        ("person", "व्यक्ति", "ವ್ಯಕ್ತಿ", "Both flat hands point down moving together down torso sides."),
        ("child", "बच्चा", "ಮಕ್ಕಳು", "Flat hand pats downward at waist level as if patting child head."),
        ("son", "बेटा", "ಮಗ", "Salute forehead then cradle arm like baby."),
        ("daughter", "बेटी", "ಮಗಳು", "Touch chin then cradle arm like baby."),
        ("husband", "पति", "ಗಂಡ", "Hand touches forehead then clasps other hand."),
        ("wife", "पत्नी", "ಹೆಂಡತಿ", "Hand touches chin then clasps other hand."),
        ("patient", "मरीज़", "ರೋಗಿ", "P-hand draws cross on shoulder or arm with calm expression."),
        ("interpreter", "दुभाषिया", "ಅನುವಾದಕ", "Both F-hands touch and twist facing each other back and forth."),
        ("relative", "रिश्तेदार", "ಸಂಬಂಧಿ", "R-hands interlock fingers twisting forward."),
        ("visitor", "आगंतुक", "ಸಂದರ್ಶಕ", "V-hand moves from distance toward self followed by PERSON sign.")
    ],
    "emotions_feelings": [
        ("happy", "खुश", "ಸಂತೋಷ", "Open flat hands brush up chest in upward flutter with smile."),
        ("sad", "उदास", "ದುಃಖ", "Open hands in front of face drop slowly downward with sad expression."),
        ("scared", "डरा हुआ", "ಹೆದರಿಕೆ", "Both open hands pull inward toward chest shaking slightly."),
        ("angry", "क्रोधित", "ಕೋಪ", "Claw hand starts at chest and twists violently upward toward face."),
        ("tired", "थका हुआ", "ದಣಿವು", "Bent hands touch chest and roll downward and slump shoulders."),
        ("comfortable", "आरामदायक", "ಆರಾಮದಾಯಕ", "Hands cup each other and stroke gently back and forth."),
        ("nervous", "घबराया हुआ", "ಆತಂಕ", "Both hands with open fingers shake gently in front of torso."),
        ("calm", "शांत", "ಶಾಂತ", "Both open palms face down and lower smoothly through air."),
        ("hungry", "भूखा", "ಹಸಿದ", "C-hand moves down middle of chest to stomach."),
        ("thirsty", "प्यासा", "ಬಾಯಾರಿಕೆ", "Index finger traces straight line down front of throat."),
        ("cold", "ठंड", "ಶೀತ", "Both fists held close to body shaking as if shivering."),
        ("hot", "गर्म", "ಬಿಸಿ", "Claw hand at mouth suddenly turns and flings away forward."),
        ("weak", "कमज़ोर", "ದುರ್ಬಲ", "Tips of fingers of right hand bend and collapse against left palm."),
        ("strong", "मजबूत", "ಬಲಶಾಲಿ", "Both fists flex forward displaying biceps."),
        ("better", "बेहतर", "ಉತ್ತಮ", "Right hand sweeps up from chin turning into thumbs up."),
        ("worse", "बदतर", "ಕೆಟ್ಟದಾಗಿದೆ", "Both K-hands cross wrists and pull sharply downward.")
    ],
    "questions": [
        ("what", "क्या", "ಏನು", "Both open palms face up shaking slightly side-to-side with quizzical look."),
        ("where", "कहाँ", "ಎಲ್ಲಿ", "Index finger held upright shaking left and right."),
        ("when", "कब", "ಯಾವಾಗ", "Right index finger circles left upright index finger and touches tip."),
        ("why", "क्यों", "ಏಕೆ", "Fingers touch forehead then pull away dropping into Y-handshape."),
        ("who", "कौन", "ಯಾರು", "Index finger circles around lips or chin questioning."),
        ("how", "कैसे", "ಹೇಗೆ", "Both curved hands back-to-back roll outward so palms face up."),
        ("how much", "कितना", "ಎಷ್ಟು", "Fingers flick upward from palms as if counting coins."),
        ("which", "कौन सा", "ಯಾವುದು", "Both thumbs up alternate moving up and down."),
        ("can you", "क्या आप कर सकते हैं", "ನೀವು ಮಾಡಬಹುದೇ", "Both fists move down firmly nodding head."),
        ("is it possible", "क्या यह संभव है", "ಇದು ಸಾಧ್ಯವೇ", "Flat hand moves forward questioning with raised eyebrows."),
        ("how many", "कितने", "ಎಷ್ಟು ಜನ", "Both open hands flick fingers upward from closed fists.")
    ],
    "time_numbers": [
        ("now", "अब", "ಈಗ", "Both Y-hands drop downward firmly."),
        ("today", "आज", "ಇಂದು", "Sign NOW twice or POINT DOWN + DAY."),
        ("tomorrow", "कल (आने वाला)", "ನಾಳೆ", "Right thumb rests on cheek then arches forward in open A-shape."),
        ("yesterday", "कल (बीता हुआ)", "ನಿನ್ನೆ", "Thumb of A-hand touches cheek then moves back to ear."),
        ("time", "समय", "ಸಮಯ", "Index finger taps back of left wrist twice where watch sits."),
        ("minute", "मिनट", "ನಿಮಿಷ", "Right index finger acts like minute hand ticking on left open palm."),
        ("hour", "घंटा", "ಗಂಟೆ", "Right index finger completes full circle on left flat palm."),
        ("day", "दिन", "ದಿನ", "Right arm rests on left arm like horizon, pointing finger sweeps across."),
        ("night", "रात", "ರಾತ್ರಿ", "Bent right wrist arches down over left horizontal arm."),
        ("morning", "सुबह", "ಬೆಳಿಗ್ಗೆ", "Right palm rises up behind left horizontal forearm."),
        ("afternoon", "दोपहर", "ಮಧ್ಯಾಹ್ನ", "Right forearm rests on left hand at slight angle forward."),
        ("week", "सप्ताह", "ವಾರ", "Right index finger slides across open left palm from wrist to fingertips."),
        ("month", "महीना", "ತಿಂಗಳು", "Right index finger slides down back of upright left index finger."),
        ("year", "साल", "ವರ್ಷ", "Right fist circles around left fist and lands on top."),
        ("zero", "शून्य", "ಶೂನ್ಯ", "Fingers curled into O shape."),
        ("one", "एक", "ಒಂದು", "Index finger upright."),
        ("two", "दो", "ಎರಡು", "Index and middle fingers upright in V shape."),
        ("three", "तीन", "ಮೂರು", "Thumb, index, and middle fingers extended."),
        ("four", "चार", "ನಾಲ್ಕು", "Four fingers extended upward with thumb folded."),
        ("five", "पाँच", "ಐದು", "All five fingers spread wide."),
        ("six", "छह", "ಆರು", "Thumb and pinky touch, three middle fingers up."),
        ("seven", "सात", "ಏಳು", "Thumb and ring finger touch."),
        ("eight", "आठ", "ಎಂಟು", "Thumb and middle finger touch."),
        ("nine", "नौ", "ಒಂಬತ್ತು", "Thumb and index finger touch."),
        ("ten", "दस", "ಹತ್ತು", "Both hands flash five or thumb extended upright shaking.")
    ],
    "actions_verbs": [
        ("come", "आओ", "ಬನ್ನಿ", "Both index fingers point outward then curl toward body."),
        ("go", "जाओ", "ಹೋಗಿ", "Both index fingers swing outward away from body."),
        ("sit", "बैठो", "ಕುಳಿತುಕೊಳ್ಳಿ", "Bent fingers of right hand drape over bent fingers of left hand."),
        ("stand", "खड़े रहो", "ನಿಲ್ಲಿ", "V-fingers of right hand stand upright on flat left palm."),
        ("walk", "चलना", "ನಡೆಯಿರಿ", "Flat hands alternate stepping forward through the air."),
        ("stop", "रुको", "ನಿಲ್ಲಿಸಿ", "Right hand chops firmly down into open palm of left hand."),
        ("wait", "प्रतीक्षा करें", "ಕಾಯಿರಿ", "Hands held forward with wiggling fingers patiently."),
        ("call", "बुलाओ", "ಕರೆಯಿರಿ", "Right hand cups mouth or waves toward chest calling someone."),
        ("write", "लिखो", "ಬರೆಯಿರಿ", "Right hand mimics holding pen and writing on left palm."),
        ("read", "पढ़ो", "ಓದಿ", "V-fingers point down moving across left open palm like scanning page."),
        ("speak", "बोलो", "ಮಾತನಾಡಿ", "Index finger taps lips or 4-hand flutters at mouth."),
        ("listen", "सुनो", "ಕೇಳಿ", "Cupped hand placed behind right ear leaning forward."),
        ("see", "देखो", "ನೋಡಿ", "V-fingers point from eyes forward toward object."),
        ("give", "दो", "ಕೊಡಿ", "Both open hands move forward extending from chest."),
        ("take", "लो", "ತೆಗೆದುಕೊಳ್ಳಿ", "Open hands reach outward then close into fists pulling inward."),
        ("open", "खोलो", "ತೆರೆಯಿರಿ", "Both flat hands touch edges then swing apart outward."),
        ("close", "बंद करो", "ಮುಚ್ಚಿ", "Both flat hands apart swing together touching edges."),
        ("start", "शुरू करो", "ಪ್ರಾರಂಭಿಸಿ", "Index finger placed between index and middle finger of left hand and twists."),
        ("finish", "ख़त्म हुआ", "ಮುಗಿಯಿತು", "Both 5-hands held chest high flick outward palms facing down."),
        ("understand", "समझना", "ಅರ್ಥಮಾಡಿಕೊಳ್ಳಿ", "Flick index finger upward next to temple like a light bulb clicking on."),
        ("remember", "याद रखना", "ನೆನಪಿಸಿಕೊಳ್ಳಿ", "Thumb of A-hand touches forehead then touches thumb of left A-hand."),
        ("forget", "भूल जाना", "ಮರೆತುಹೋಗಿದೆ", "Flat hand wipes across forehead from left to right as if erasing.")
    ],
    "food_nutrition": [
        ("milk", "दूध", "ಹಾಲು", "Right fist opens and closes twice mimicking milking motion."),
        ("tea", "चाय", "ಚಹಾ", "F-hand holds imaginary teabag dipping into left cupped C-hand."),
        ("coffee", "कॉफ़ी", "ಕಾಫಿ", "Both fists rotate on top of each other like grinding beans."),
        ("rice", "चावल", "ಅನ್ನ", "Hand scoops imaginary grain from palm to mouth."),
        ("bread", "रोटी / ब्रेड", "ರೊಟ್ಟಿ / ಬ್ರೆಡ್", "Side of right pinky slices downward across back of left wrist."),
        ("fruit", "फल", "ಹಣ್ಣು", "F-hand twists against right cheek with sweet expression."),
        ("vegetables", "सब्ज़ियाँ", "ತರಕಾರಿಗಳು", "V-handshape twists at cheek corner."),
        ("apple", "सेब", "ಸೇಬು", "Knuckle of bent index finger twists against cheek."),
        ("banana", "केला", "ಬಾಳೆಹಣ್ಣು", "Left index finger acts as banana, right fingers peel down sides."),
        ("soup", "सूप", "ಸೂಪ್", "Curved fingers mimic spoon scooping from left palm to mouth."),
        ("sugar", "चीनी", "ಸಕ್ಕರೆ", "Fingertips rub downward across chin twice."),
        ("salt", "नमक", "ಉಪ್ಪು", "Two fingers of right hand tap two fingers of left hand twice."),
        ("water bottle", "पानी की बोतल", "ನೀರಿನ ಬಾಟಲ್", "Sign WATER followed by C-hands forming cylinder."),
        ("juice", "जूस", "ಜ್ಯೂಸ್", "J-letter handshape drawn from corner of mouth.")
    ],
    "alphabet_signs": [
        ("a", "ए", "ಎ", "Fist with thumb resting along side of index finger."),
        ("b", "बी", "ಬಿ", "Flat hand with four fingers straight up, thumb folded across palm."),
        ("c", "सी", "ಸಿ", "Curved hand forming C shape."),
        ("d", "डी", "ಡಿ", "Index finger points straight up, thumb touches other three curled fingers."),
        ("e", "ई", "ಇ", "Curled fingers rest tips on thumb."),
        ("f", "एफ़", "ಎಫ್", "Index and thumb form circle, other three fingers upright."),
        ("g", "जी", "ಜಿ", "Index finger and thumb extend parallel horizontally pointing left."),
        ("h", "एच", "ಎಚ್", "Index and middle fingers extend horizontally side-by-side."),
        ("i", "आई", "ಐ", "Pinky finger points straight up from closed fist."),
        ("j", "जे", "ಜೆ", "Pinky finger traces letter J path in the air."),
        ("k", "के", "ಕೆ", "Index finger upright, middle finger forward, thumb at base of middle."),
        ("l", "एल", "ಎಲ್", "Index finger and thumb extend forming right-angle L shape."),
        ("m", "एम", "ಎಮ್", "Thumb tucked under three middle fingers extending over it."),
        ("n", "एन", "ಎನ್", "Thumb tucked under index and middle fingers extending over it."),
        ("o", "ओ", "ಒ", "All fingertips touch thumb forming O circle."),
        ("p", "पी", "ಪಿ", "K handshape pointing downward."),
        ("q", "क्यू", "ಕ್ಯೂ", "G handshape pointing downward."),
        ("r", "आर", "ಆರ್", "Index and middle fingers crossed."),
        ("s", "एस", "ಎಸ್", "Closed fist with thumb wrapped across front of fingers."),
        ("t", "टी", "ಟಿ", "Thumb tucked between index and middle fingers of fist."),
        ("u", "यू", "ಯು", "Index and middle fingers held straight up together."),
        ("v", "वी", "ವಿ", "Index and middle fingers held straight up spread in V shape."),
        ("w", "डब्ल्यू", "ಡಬ್ಲ್ಯೂ", "Index, middle, and ring fingers spread upright forming W."),
        ("x", "एक्स", "ಎಕ್ಸ್", "Index finger bent like a hook from closed fist."),
        ("y", "वाई", "ವೈ", "Thumb and pinky extended, middle three fingers folded."),
        ("z", "ज़ेड", "ಝಡ್", "Index finger traces the shape of Z in the air.")
    ]
}

vocab_list = []
entry_id = 1
for cat, items in vocab_data.items():
    for en, hi, kn, desc in items:
        vocab_list.append({
            "id": entry_id,
            "category": cat,
            "word": en,
            "hindi": hi,
            "kannada": kn,
            "sign_description": desc,
            "keywords": [w.strip() for w in en.split()] + [cat]
        })
        entry_id += 1

with open("speech_to_sign_vocab.json", "w", encoding="utf-8") as f:
    json.dump({"total_entries": len(vocab_list), "categories": list(vocab_data.keys()), "vocabulary": vocab_list}, f, indent=2, ensure_ascii=False)

print(f"Generated speech_to_sign_vocab.json with {len(vocab_list)} entries across {len(vocab_data)} categories.")


hospital_categories = {
    "emergency_urgent": [
        ("Emergency! Please call a doctor immediately.", "आपातकाल! कृपया तुरंत डॉक्टर को बुलाएं।", "ತುರ್ತು ಪರಿಸ್ಥಿತಿ! ದಯವಿಟ್ಟು ತಕ್ಷಣ ವೈದ್ಯರನ್ನು ಕರೆಯಿರಿ.", "High", "EMERGENCY + CALL + DOCTOR + QUICK"),
        ("I cannot breathe properly.", "मुझे ठीक से सांस नहीं आ रही है।", "ನನಗೆ ಸರಿಯಾಗಿ ಉಸಿರಾಡಲು ಸಾಧ್ಯವಾಗುತ್ತಿಲ್ಲ.", "High", "ME + BREATHE + DIFFICULT"),
        ("I am experiencing severe chest pain.", "मुझे सीने में बहुत तेज दर्द हो रहा है।", "ನನಗೆ ಎದೆಯಲ್ಲಿ ತೀವ್ರ ನೋವು ಕಾಣಿಸಿಕೊಂಡಿದೆ.", "High", "ME + CHEST + PAIN + SEVERE"),
        ("Please help me, I feel like fainting.", "कृपया मेरी मदद करें, मुझे चक्कर आ रहे हैं।", "ದಯವಿಟ್ಟು ನನಗೆ ಸಹಾಯ ಮಾಡಿ, ನನಗೆ ಪ್ರಜ್ಞೆ ತಪ್ಪಿದಂತೆ ಅನಿಸುತ್ತಿದೆ.", "High", "PLEASE + HELP + ME + DIZZY + FAINT"),
        ("There is heavy bleeding here.", "यहाँ बहुत अधिक खून बह रहा है।", "ಇಲ್ಲಿ ಹೆಚ್ಚು ರಕ್ತಸ್ರಾವವಾಗುತ್ತಿದೆ.", "High", "HERE + BLOOD + MUCH + FLOW"),
        ("I need an oxygen mask right now.", "मुझे अभी ऑक्सीजन मास्क चाहिए।", "ನನಗೆ ಈಗಲೇ ಆಮ್ಲಜನಕದ ಮಾಸ್ಕ್ ಬೇಕು.", "High", "ME + OXYGEN + MASK + NEED + NOW"),
        ("The patient is unresponsive.", "मरीज़ कोई प्रतिक्रिया नहीं दे रहा है।", "ರೋಗಿಯು ಯಾವುದೇ ಪ್ರತಿಕ್ರಿಯೆ ನೀಡುತ್ತಿಲ್ಲ.", "High", "PATIENT + RESPONSE + NO"),
        ("I feel sudden numbness in my face and arm.", "मेरे चेहरे और हाथ में अचानक सुन्नपन महसूस हो रहा है।", "ನನ್ನ ಮುಖ ಮತ್ತು ತೋಳಿನಲ್ಲಿ ಹಠಾತ್ ಮರಗಟ್ಟುವಿಕೆ ಅನಿಸುತ್ತಿದೆ.", "High", "FACE + ARM + NUMB + SUDDEN"),
        ("Severe allergic reaction happening.", "गंभीर एलर्जी की प्रतिक्रिया हो रही है।", "ತೀವ್ರ ಅಲರ್ಜಿ ಉಂಟಾಗುತ್ತಿದೆ.", "High", "ALLERGY + SEVERE + HAPPEN"),
        ("Please call the ambulance quickly.", "कृपया जल्दी एम्बुलेंस बुलाएं।", "ದಯವಿಟ್ಟು ಬೇಗ ಆಂಬ್ಯುಲೆನ್ಸ್ ಕರೆಯಿರಿ.", "High", "PLEASE + AMBULANCE + CALL + QUICK")
    ],
    "symptoms_pain": [
        ("Where does it hurt the most?", "सबसे ज्यादा दर्द कहाँ हो रहा है?", "ಎಲ್ಲಿ ಹೆಚ್ಚು ನೋವು ಆಗುತ್ತಿದೆ?", "Medium", "WHERE + PAIN + MOST"),
        ("My pain level is 8 out of 10.", "मेरा दर्द 10 में से 8 है।", "ನನ್ನ ನೋವಿನ ಪ್ರಮಾಣ 10 ರಲ್ಲಿ 8 ಇದೆ.", "High", "PAIN + NUMBER 8 + LEVEL"),
        ("I have a throbbing headache.", "मेरे सिर में तेज दर्द हो रहा है।", "ನನಗೆ ತಲೆನೋವು ವಿಪರೀತವಾಗಿದೆ.", "Medium", "HEAD + PAIN + THROBBING"),
        ("I have severe stomach cramps.", "मेरे पेट में बहुत तेज मरोड़ और दर्द है।", "ನನ್ನ ಹೊಟ್ಟೆಯಲ್ಲಿ ತೀವ್ರ ಸೆಳೆತದ ನೋವಿದೆ.", "Medium", "STOMACH + PAIN + CRAMP"),
        ("I have high fever and shivering chills.", "मुझे तेज बुखार और कंपकंपी है।", "ನನಗೆ ತೀವ್ರ ಜ್ವರ ಮತ್ತು ನಡುಕವಿದೆ.", "Medium", "FEVER + HIGH + COLD + SHIVER"),
        ("I feel persistent nausea and vomiting.", "मुझे लगातार उल्टी और मतली महसूस हो रही है।", "ನನಗೆ ವಾಂತಿ ಮತ್ತು ವಾಕರಿಕೆ ಬರುತ್ತಿದೆ.", "Medium", "NAUSEA + VOMITING + PERSIST"),
        ("My back pain makes it impossible to stand.", "मेरी पीठ में इतना दर्द है कि खड़ा नहीं हो पा रहा हूँ।", "ನನ್ನ ಬೆನ್ನುನೋವಿನಿಂದಾಗಿ ನಿಲ್ಲಲು ಸಾಧ್ಯವಾಗುತ್ತಿಲ್ಲ.", "Medium", "BACK + PAIN + STAND + CANNOT"),
        ("I have a burning sensation when urinating.", "पेशाब करते समय जलन महसूस होती है।", "ಮೂತ್ರ ವಿಸರ್ಜನೆ ಮಾಡುವಾಗ ಉರಿ ಅನಿಸುತ್ತದೆ.", "Medium", "URINE + BURNING + PAIN"),
        ("My throat is swollen and painful to swallow.", "मेरा गला सूजा हुआ है और निगलने में दर्द है।", "ನನ್ನ ಗಂಟಲು ಊದಿಕೊಂಡಿದೆ ಮತ್ತು ನುಂಗಲು ನೋವಾಗುತ್ತಿದೆ.", "Medium", "THROAT + SWOLLEN + SWALLOW + PAIN"),
        ("I feel sharp shooting pain in my leg.", "मेरे पैर में तेज चुभन वाला दर्द है।", "ನನ್ನ ಕಾಲಿನಲ್ಲಿ ಚುಚ್ಚುವಂತಹ ತೀವ್ರ ನೋವಿದೆ.", "Medium", "LEG + PAIN + SHARP")
    ],
    "doctor_patient_dialogue": [
        ("The doctor will examine you shortly.", "डॉक्टर जल्द ही आपकी जांच करेंगे।", "ವೈದ್ಯರು ಶೀಘ್ರದಲ್ಲೇ ನಿಮ್ಮನ್ನು ಪರೀಕ್ಷಿಸುತ್ತಾರೆ.", "Low", "DOCTOR + SOON + EXAMINE + YOU"),
        ("How long have you had this pain?", "आपको यह दर्द कब से है?", "ನಿಮಗೆ ಈ ನೋವು ಎಷ್ಟು ದಿನಗಳಿಂದ ಇದೆ?", "Medium", "HOW-LONG + YOU + PAIN + HAVE"),
        ("Do you have any existing chronic illnesses?", "क्या आपको पहले से कोई पुरानी बीमारी है?", "ನಿಮಗೆ ಯಾವುದಾದರೂ ಹಳೆಯ ದೀರ್ಘಕಾಲದ ಕಾಯಿಲೆಗಳಿವೆಯೆ?", "Medium", "YOU + PAST + ILLNESS + HAVE?"),
        ("Are you allergic to any medicines?", "क्या आपको किसी दवा से एलर्जी है?", "ನಿಮಗೆ ಯಾವುದೇ ಔಷಧಿಗಳಿಗೆ ಅಲರ್ಜಿ ಇದೆಯೇ?", "High", "YOU + MEDICINE + ALLERGY + HAVE?"),
        ("Please open your mouth and stick out your tongue.", "कृपया अपना मुंह खोलें और जीभ बाहर निकालें।", "ದಯವಿಟ್ಟು ನಿಮ್ಮ ಬಾಯಿ ತೆರೆದು ನಾಲಿಗೆಯನ್ನು ಹೊರಗೆ ತೋರಿಸಿ.", "Low", "MOUTH + OPEN + TONGUE + SHOW"),
        ("Take a deep breath in and hold it.", "एक गहरी सांस लें और रोक कर रखें।", "ದೀರ್ಘವಾಗಿ ಉಸಿರನ್ನು ತೆಗೆದುಕೊಂಡು ನಿಲ್ಲಿಸಿ.", "Low", "BREATHE + DEEP + HOLD"),
        ("Your test reports look stable.", "आपकी जांच रिपोर्ट सामान्य दिख रही है।", "ನಿಮ್ಮ ಪರೀಕ್ಷಾ ವರದಿಗಳು ಸ್ಥಿರವಾಗಿವೆ.", "Low", "REPORT + TEST + STABLE + GOOD"),
        ("You will need a minor procedure.", "आपको एक छोटी प्रक्रिया की आवश्यकता होगी।", "ನಿಮಗೆ ಸಣ್ಣ ಶಸ್ತ್ರಚಿಕಿತ್ಸಾ ಪ್ರಕ್ರಿಯೆ ಅಗತ್ಯವಿದೆ.", "Medium", "YOU + PROCEDURE + SMALL + NEED"),
        ("Do not worry, you are in safe hands.", "चिंता न करें, आप सुरक्षित हाथों में हैं।", "ಚಿಂತೆ ಮಾಡಬೇಡಿ, ನೀವು ಸುರಕ್ಷಿತ ಕೈಗಳಲ್ಲಿದ್ದೀರಿ.", "Low", "NOT + WORRY + YOU + SAFE"),
        ("Please sign the consent form here.", "कृपया यहाँ सहमति पत्र पर हस्ताक्षर करें।", "ದಯವಿಟ್ಟು ಇಲ್ಲಿ ಒಪ್ಪಿಗೆ ಪತ್ರಕ್ಕೆ ಸಹಿ ಮಾಡಿ.", "Low", "CONSENT + PAPER + SIGN + HERE")
    ],
    "nursing_assistance": [
        ("I need assistance going to the restroom.", "मुझे शौचालय जाने के लिए सहायता चाहिए।", "ನನಗೆ ಶೌಚಾಲಯಕ್ಕೆ ಹೋಗಲು ಸಹಾಯ ಬೇಕು.", "Medium", "ME + RESTROOM + GO + HELP + NEED"),
        ("The nurse is coming to check your IV drip.", "नर्स आपकी आईवी ड्रिप जांचने आ रही है।", "ಶುಶ್ರೂಷಕಿ ನಿಮ್ಮ ಐವಿ ಡ್ರಿಪ್ ಪರೀಕ್ಷಿಸಲು ಬರುತ್ತಿದ್ದಾರೆ.", "Low", "NURSE + COME + DRIP + CHECK"),
        ("Can you please change my bedsheets?", "क्या आप कृपया मेरी चादरें बदल सकते हैं?", "ದಯವಿಟ್ಟು ನನ್ನ ಹಾಸಿಗೆಯ ಹಾಳೆಯನ್ನು ಬದಲಾಯಿಸಬಹುದೇ?", "Low", "BED + SHEET + CHANGE + PLEASE"),
        ("My IV cannula is hurting and swollen.", "मेरा आईवी कैन्युला दर्द कर रहा है और सूज गया है।", "ನನ್ನ ಐವಿ ಸೂಜಿ ಚುಚ್ಚಿದ ಜಾಗ ನೋಯುತ್ತಿದೆ ಮತ್ತು ಊದಿಕೊಂಡಿದೆ.", "Medium", "IV + CANNULA + PAIN + SWOLLEN"),
        ("Please help me sit upright in bed.", "कृपया मुझे बिस्तर पर सीधे बैठने में मदद करें।", "ದಯವಿಟ್ಟು ನಾನು ಹಾಸಿಗೆಯಲ್ಲಿ ನೆಟ್ಟಗೆ ಕುಳಿತುಕೊಳ್ಳಲು ಸಹಾಯ ಮಾಡಿ.", "Low", "HELP + ME + BED + SIT + UP"),
        ("I accidentally spilled water on the bed.", "मुझसे गलती से बिस्तर पर पानी गिर गया।", "ಆಕಸ್ಮಿಕವಾಗಿ ಹಾಸಿಗೆಯ ಮೇಲೆ ನೀರು ಚೆಲ್ಲಿದೆ.", "Low", "WATER + BED + SPILL + ACCIDENT"),
        ("Can you please adjust the room temperature?", "क्या आप कमरे का तापमान ठीक कर सकते हैं?", "ದಯವಿಟ್ಟು ಕೊಠಡಿಯ ತಾಪಮಾನವನ್ನು ಸರಿಹೊಂದಿಸಬಹುದೇ?", "Low", "ROOM + TEMPERATURE + ADJUST + PLEASE"),
        ("I need a clean gown or towel.", "मुझे एक साफ गाउन या तौलिया चाहिए।", "ನನಗೆ ಸ್ವಚ್ಛವಾದ ಗೌನ್ ಅಥವಾ ಟವೆಲ್ ಬೇಕು.", "Low", "CLEAN + GOWN + TOWEL + NEED"),
        ("Please call the on-duty nurse right away.", "कृपया ड्यूटी पर मौजूद नर्स को तुरंत बुलाएं।", "ದಯವಿಟ್ಟು ಕರ್ತವ್ಯದಲ್ಲಿರುವ ನರ್ಸ್ ಅವರನ್ನು ತಕ್ಷಣ ಕರೆಯಿರಿ.", "Medium", "NURSE + DUTY + CALL + NOW"),
        ("The bed buzzer / call bell is not working.", "बिस्तर की कॉल बेल काम नहीं कर रही है।", "ಹಾಸಿಗೆಯ ಕರೆ ಗಂಟೆ ಕೆಲಸ ಮಾಡುತ್ತಿಲ್ಲ.", "Medium", "CALL + BELL + WORK + NOT")
    ],
    "medication_pharmacy": [
        ("It is time to take your morning medication.", "यह आपकी सुबह की दवा लेने का समय है।", "ನಿಮ್ಮ ಬೆಳಗಿನ ಔಷಧಿ ತೆಗೆದುಕೊಳ್ಳುವ ಸಮಯವಾಯಿತು.", "Low", "TIME + MORNING + MEDICINE + TAKE"),
        ("Should I take this medicine before or after meals?", "क्या मुझे यह दवा खाने से पहले या बाद में लेनी चाहिए?", "ನಾನು ಈ ಔಷಧಿಯನ್ನು ಊಟಕ್ಕೆ ಮುಂಚೆ ಅಥವಾ ನಂತರ ತೆಗೆದುಕೊಳ್ಳಬೇಕೆ?", "Low", "MEDICINE + FOOD + BEFORE + AFTER?"),
        ("This medicine is causing dizziness.", "इस दवा से चक्कर आ रहे हैं।", "ಈ ಔಷಧಿಯಿಂದ ನನಗೆ ತಲೆಸುತ್ತು ಬರುತ್ತಿದೆ.", "Medium", "THIS + MEDICINE + CAUSE + DIZZY"),
        ("I need my painkiller medicine now.", "मुझे अभी दर्द निवारक दवा की आवश्यकता है।", "ನನಗೆ ಈಗ ನೋವು ನಿವಾರಕ ಔಷಧಿ ಬೇಕು.", "Medium", "ME + PAINKILLER + MEDICINE + NEED + NOW"),
        ("Is there an alternative syrup instead of this tablet?", "क्या इस गोली की जगह कोई सिरप उपलब्ध है?", "ಈ ಮಾತ್ರೆಗೆ ಬದಲಾಗಿ ಸಿರಪ್ ಲಭ್ಯವಿದೆಯೇ?", "Low", "TABLET + INSTEAD + SYRUP + HAVE?"),
        ("You need to take this medicine three times daily.", "आपको यह दवा दिन में तीन बार लेनी है।", "ನೀವು ಈ ಔಷಧಿಯನ್ನು ದಿನಕ್ಕೆ ಮೂರು ಬಾರಿ ತೆಗೆದುಕೊಳ್ಳಬೇಕು.", "Low", "MEDICINE + TAKE + 3 TIMES + DAY"),
        ("Please bring my insulin injection.", "कृपया मेरा इंसुलिन इंजेक्शन लाएं।", "ದಯವಿಟ್ಟು ನನ್ನ ಇನ್ಸುಲಿನ್ ಚುಚ್ಚುಮದ್ದನ್ನು ತನ್ನಿ.", "Medium", "INSULIN + INJECTION + BRING + PLEASE"),
        ("I have finished my course of antibiotics.", "मेरा एंटीबायोटिक का कोर्स पूरा हो गया है।", "ನನ್ನ ಆ್ಯಂಟಿಬಯೋಟಿಕ್ ಚಿಕಿತ್ಸೆ ಮುಕ್ತಾಯಗೊಂಡಿದೆ.", "Low", "ANTIBIOTIC + MEDICINE + FINISH"),
        ("This ointment needs to be applied twice a day.", "यह मलहम दिन में दो बार लगाना होगा।", "ಈ ಮುಲಾಮನ್ನು ದಿನಕ್ಕೆ ಎರಡು ಬಾರಿ ಹಚ್ಚಬೇಕು.", "Low", "OINTMENT + APPLY + TWICE + DAY")
    ],
    "diagnostic_tests": [
        ("You need to get a blood test done.", "आपको रक्त परीक्षण (ब्लड टेस्ट) करवाना होगा।", "ನೀವು ರಕ್ತ ಪರೀಕ್ಷೆ ಮಾಡಿಸಿಕೊಳ್ಳಬೇಕು.", "Low", "YOU + BLOOD + TEST + NEED"),
        ("We need to take an X-ray of your chest.", "हमें आपकी छाती का एक्स-रे लेना होगा।", "ನಾವು ನಿಮ್ಮ ಎದೆಯ ಎಕ್ಸ್-ರೇ ತೆಗೆದುಕೊಳ್ಳಬೇಕು.", "Low", "CHEST + XRAY + TAKE + NEED"),
        ("Please remain completely still during the MRI scan.", "एमआरआई स्कैन के दौरान बिल्कुल स्थिर रहें।", "ಎಂಆರ್‌ಐ ಸ್ಕ್ಯಾನ್ ಸಮಯದಲ್ಲಿ ಸಂಪೂರ್ಣವಾಗಿ ಶಾಂತರಾಗಿರಿ.", "Low", "MRI + SCAN + TIME + STILL + STAY"),
        ("You must remain fasting for the ultrasound test.", "अल्ट्रासाउंड परीक्षण के लिए आपको भूखा रहना होगा।", "ಅಲ್ಟ್ರಾಸೌಂಡ್ ಪರೀಕ್ಷೆಗೆ ನೀವು ಉಪವಾಸವಿರಬೇಕು.", "Low", "ULTRASOUND + FASTING + FOOD + NO"),
        ("Urine sample needs to be collected in this bottle.", "इस बोतल में मूत्र का नमूना देना होगा।", "ಈ ಬಾಟಲಿಯಲ್ಲಿ ಮೂತ್ರದ ಮಾದರಿಯನ್ನು ಸಂಗ್ರಹಿಸಬೇಕು.", "Low", "URINE + SAMPLE + BOTTLE + GIVE"),
        ("The ECG recording shows normal rhythm.", "ईसीजी रिकॉर्डिंग सामान्य ताल दिखा रही है।", "ಇಸಿಜಿ ವರದಿ ಸಹಜ ಸ್ಥಿತಿಯನ್ನು ತೋರಿಸುತ್ತಿದೆ.", "Low", "ECG + HEART + RHYTHM + NORMAL"),
        ("When will the biopsy laboratory results come?", "बायोप्सी प्रयोगशाला के परिणाम कब आएंगे?", "ಬಯಾಪ್ಸಿ ಪ್ರಯೋಗಾಲಯದ ವರದಿಗಳು ಯಾವಾಗ ಬರುತ್ತವೆ?", "Low", "BIOPSY + RESULT + WHEN + COME?"),
        ("CT scan is scheduled for 2:00 PM today.", "सीटी स्कैन आज दोपहर 2:00 बजे निर्धारित है।", "ಸಿಟಿ ಸ್ಕ್ಯಾನ್ ಇಂದು ಮಧ್ಯಾಹ್ನ 2:00 ಕ್ಕೆ ನಿಗದಿಯಾಗಿದೆ.", "Low", "CT-SCAN + TODAY + 2 PM + TIME")
    ],
    "vital_signs_monitoring": [
        ("I am going to check your blood pressure now.", "मैं अब आपका रक्तचाप (बीपी) जांचने जा रहा हूँ।", "ನಾನು ಈಗ ನಿಮ್ಮ ರಕ್ತದೊತ್ತಡವನ್ನು ಪರೀಕ್ಷಿಸಲಿದ್ದೇನೆ.", "Low", "ME + BP + CHECK + NOW"),
        ("Your blood pressure is within normal range.", "आपका रक्तचाप सामान्य सीमा के भीतर है।", "ನಿಮ್ಮ ರಕ್ತದೊತ್ತಡ ಸಹಜ ಮಟ್ಟದಲ್ಲಿದೆ.", "Low", "BP + NORMAL + STABLE"),
        ("Your body temperature is 101 degrees Fahrenheit.", "आपके शरीर का तापमान 101 डिग्री फ़ारेनहाइट है।", "ನಿಮ್ಮ ದೇಹದ ಉಷ್ಣತೆ 101 ಡಿಗ್ರಿ ಇದೆ.", "Medium", "TEMPERATURE + 101 + HIGH"),
        ("Your oxygen saturation level is 98 percent.", "आपका ऑक्सीजन स्तर 98 प्रतिशत है।", "ನಿಮ್ಮ ಆಮ್ಲಜನಕದ ಮಟ್ಟ ಶೇಕಡಾ 98 ರಷ್ಟಿದೆ.", "Low", "OXYGEN + LEVEL + 98 + GOOD"),
        ("Your pulse rate is slightly faster than usual.", "आपकी नब्ज़ सामान्य से थोड़ी तेज़ चल रही है।", "ನಿಮ್ಮ ನಾಡಿಮಿಡಿತ ಸಾಮಾನ್ಯಕ್ಕಿಂತ ಸ್ವಲ್ಪ ಹೆಚ್ಚಾಗಿದೆ.", "Low", "PULSE + HEART + FAST + SLIGHT"),
        ("Please extend your finger for the pulse oximeter.", "पल्स ऑक्सीमीटर के लिए कृपया अपनी उंगली आगे बढ़ाएं।", "ಪಲ್ಸ್ ಆಕ್ಸಿಮೀಟರ್‌ಗಾಗಿ ನಿಮ್ಮ ಬೆರಳನ್ನು ಮುಂದೆ ಚಾಚಿ.", "Low", "FINGER + OXIMETER + PUT + PLEASE"),
        ("We need to monitor your blood sugar level.", "हमें आपके ब्लड शुगर की जांच करनी होगी।", "ನಾವು ನಿಮ್ಮ ರಕ್ತದ ಸಕ್ಕರೆ ಮಟ್ಟವನ್ನು ಪರೀಕ್ಷಿಸಬೇಕು.", "Low", "BLOOD + SUGAR + MONITOR + NEED"),
        ("Everything looks stable on the monitor screen.", "मॉनिटर स्क्रीन पर सब कुछ स्थिर दिख रहा है।", "ಮಾನಿಟರ್ ಪರದೆಯ ಮೇಲೆ ಎಲ್ಲವೂ ಸ್ಥಿರವಾಗಿ ಕಾಣುತ್ತಿದೆ.", "Low", "MONITOR + VITAL + STABLE + GOOD")
    ],
    "food_diet": [
        ("Can I get warm drinking water?", "क्या मुझे पीने के लिए गुनगुना पानी मिल सकता है?", "ನನಗೆ ಕುಡಿಯಲು ಬೆಚ್ಚಗಿನ ನೀರು ಸಿಗಬಹುದೇ?", "Low", "WARM + WATER + DRINK + WANT"),
        ("Are you on a diabetic diet?", "क्या आपका मधुमेह (शुगर) वाला विशेष आहार है?", "ನಿಮಗೆ ಸಕ್ಕರೆ ಕಾಯಿಲೆಗೆ ತಕ್ಕ ಆಹಾರ ಪಥ್ಯವಿದೆಯೇ?", "Low", "DIABETIC + DIET + FOOD + YOU?"),
        ("I feel very hungry, when is dinner served?", "मुझे बहुत भूख लगी है, रात का खाना कब मिलेगा?", "ನನಗೆ ತುಂಬಾ ಹಸಿವಾಗಿದೆ, ರಾತ್ರಿಯ ಊಟ ಯಾವಾಗ?", "Low", "HUNGRY + DINNER + FOOD + WHEN?"),
        ("I need a straw to drink liquids.", "मुझे तरल पदार्थ पीने के लिए स्ट्रॉ चाहिए।", "ನನಗೆ ದ್ರವ ಪದಾರ್ಥ ಕುಡಿಯಲು ಸ್ಟ್ರಾ ಬೇಕು.", "Low", "STRAW + DRINK + LIQUID + NEED"),
        ("Doctor advised light liquid diet today.", "डॉक्टर ने आज केवल हल्का तरल आहार लेने की सलाह दी है।", "ವೈದ್ಯರು ಇಂದು ಲಘು ದ್ರವ ಆಹಾರವನ್ನು ಮಾತ್ರ ಸೂಚಿಸಿದ್ದಾರೆ.", "Low", "DOCTOR + ADVISE + LIQUID + FOOD + TODAY"),
        ("Can I have a cup of warm milk or tea?", "क्या मुझे एक कप गर्म दूध या चाय मिल सकती है?", "ನನಗೆ ಒಂದು ಕಪ್ ಬಿಸಿ ಹಾಲು ಅಥವಾ ಚಹಾ ಸಿಗಬಹುದೇ?", "Low", "WARM + MILK + TEA + WANT"),
        ("I cannot eat solid food due to pain.", "दर्द के कारण मैं ठोस भोजन नहीं खा पा रहा हूँ।", "ನೋವಿನ ಕಾರಣ ನನಗೆ ಗಟ್ಟಿ ಆಹಾರ ಸೇವಿಸಲು ಸಾಧ್ಯವಾಗುತ್ತಿಲ್ಲ.", "Medium", "SOLID + FOOD + EAT + CANNOT + PAIN"),
        ("Please remove the finished meal tray.", "कृपया खाली खाने की ट्रे हटा दें।", "ದಯವಿಟ್ಟು ಊಟವಾದ ಖಾಲಿ ತಟ್ಟೆಯನ್ನು ತೆಗೆದುಕೊಂಡು ಹೋಗಿ.", "Low", "FOOD + TRAY + FINISH + REMOVE"),
        ("Can I get soft porridge or khichdi?", "क्या मुझे पतली खिचड़ी या दलिया मिल सकता है?", "ನನಗೆ ಮೃದುವಾದ ಕಿಚಡಿ ಅಥವಾ ಗಂಜಿ ಸಿಗಬಹುದೇ?", "Low", "SOFT + KHICHDI + PORRIDGE + WANT"),
        ("Is sugar-free tea available here?", "क्या यहाँ बिना चीनी की चाय मिल सकती है?", "ಇಲ್ಲಿ ಸಕ್ಕರೆ ರಹಿತ ಚಹಾ ಲಭ್ಯವಿದೆಯೇ?", "Low", "SUGAR-FREE + TEA + AVAILABLE?")
    ],
    "mobility_comfort": [
        ("I need a wheelchair to go to the scan room.", "मुझे स्कैन कक्ष में जाने के लिए व्हीलचेयर चाहिए।", "ಸ್ಕ್ಯಾನ್ ಕೊಠಡಿಗೆ ಹೋಗಲು ನನಗೆ ವೀಲ್ ಚೇರ್ ಬೇಕು.", "Low", "WHEELCHAIR + NEED + SCAN + ROOM"),
        ("Please help me turn onto my other side.", "कृपया मुझे दूसरी करवट लेने में मदद करें।", "ದಯವಿಟ್ಟು ನಾನು ಇನ್ನೊಂದು ಬದಿಗೆ ಹೊರಳಲು ಸಹಾಯ ಮಾಡಿ.", "Low", "TURN + SIDE + HELP + ME"),
        ("Can you adjust my pillow height?", "क्या आप मेरे तकिए की ऊंचाई ठीक कर सकते हैं?", "ನನ್ನ ದಿಂಬಿನ ಎತ್ತರವನ್ನು ಸರಿಹೊಂದಿಸಬಹುದೇ?", "Low", "PILLOW + HEIGHT + ADJUST + PLEASE"),
        ("I feel too cold, please provide an extra blanket.", "मुझे बहुत ठंड लग रही है, कृपया एक अतिरिक्त कंबल दें।", "ನನಗೆ ತುಂಬಾ ಚಳಿಯಾಗುತ್ತಿದೆ, ದಯವಿಟ್ಟು ಮತ್ತೊಂದು ಕಂಬಳಿ ಕೊಡಿ.", "Low", "COLD + EXTRA + BLANKET + PLEASE"),
        ("Can you help me walk a few steps?", "क्या आप मुझे कुछ कदम चलने में मदद कर सकते हैं?", "ನಾನು ಕೆಲವು ಹೆಜ್ಜೆ ನಡೆಯಲು ಸಹಾಯ ಮಾಡುವಿರಾ?", "Low", "WALK + FEW + STEPS + HELP + ME"),
        ("I need crutches or a walking walker.", "मुझे बैसाखी या वॉकर की आवश्यकता है।", "ನನಗೆ ಊರುಗೋಲು ಅಥವಾ ವಾಕರ್ ಅಗತ್ಯವಿದೆ.", "Low", "CRUTCHES + WALKER + NEED"),
        ("The light is shining in my eyes, please close curtains.", "रोशनी आँखों में चुभ रही है, कृपया पर्दा लगा दें।", "ಬೆಳಕು ಕಣ್ಣಿಗೆ ತಾಗುತ್ತಿದೆ, ದಯವಿಟ್ಟು ಪರದೆ ಹಾಕಿ.", "Low", "LIGHT + BRIGHT + CURTAIN + CLOSE"),
        ("Please raise the head of my bed slightly.", "कृपया मेरे बिस्तर का सिरा थोड़ा ऊपर उठाएं।", "ದಯವಿಟ್ಟು ನನ್ನ ಹಾಸಿಗೆಯ ತಲೆಯ ಭಾಗವನ್ನು ಸ್ವಲ್ಪ ಎತ್ತರಿಸಿ.", "Low", "BED + HEAD + RAISE + PLEASE"),
        ("The room is too noisy, can we close the door?", "कमरे में बहुत शोर है, क्या दरवाजा बंद कर सकते हैं?", "ಕೋಣೆಯಲ್ಲಿ ತುಂಬಾ ಶಬ್ದವಿದೆ, ಬಾಗಿಲು ಮುಚ್ಚಬಹುದೇ?", "Low", "ROOM + NOISY + DOOR + CLOSE"),
        ("I need help sitting on the edge of the bed.", "मुझे बिस्तर के किनारे बैठने में मदद चाहिए।", "ನನಗೆ ಹಾಸಿಗೆಯ ಅಂಚಿನಲ್ಲಿ ಕುಳಿತುಕೊಳ್ಳಲು ಸಹಾಯ ಬೇಕು.", "Low", "BED + EDGE + SIT + HELP")
    ],
    "hygiene_restroom": [
        ("I urgently need to use the washroom.", "मुझे तुरंत शौचालय जाना है।", "ನಾನು ತಕ್ಷಣ ಶೌಚಾಲಯಕ್ಕೆ ಹೋಗಬೇಕು.", "Medium", "URGENT + RESTROOM + GO + NEED"),
        ("I need a bedpan or urinal immediately.", "मुझे तुरंत बेडपैन या यूरिनल की आवश्यकता है।", "ನನಗೆ ತಕ್ಷಣ ಬೆಡ್‌ಪ್ಯಾನ್ ಅಥವಾ ಮೂತ್ರಪಾತ್ರೆ ಬೇಕು.", "Medium", "BEDPAN + URINAL + NEED + NOW"),
        ("Can someone help me sponge bathe and clean?", "क्या कोई मुझे स्पंज स्नान कराने में मदद कर सकता है?", "ಯಾರಾದರೂ ನಾನು ಮೈ ಒರೆಸಿಕೊಳ್ಳಲು ಸಹಾಯ ಮಾಡುವಿರಾ?", "Low", "SPONGE + BATH + CLEAN + HELP"),
        ("My diaper needs to be changed.", "मेरा डायपर बदलने की जरूरत है।", "ನನ್ನ ಡೈಪರ್ ಬದಲಾಯಿಸಬೇಕಾಗಿದೆ.", "Low", "DIAPER + CHANGE + NEED"),
        ("Please provide hand sanitizer and soap.", "कृपया हैंड सैनिटाइज़र और साबुन उपलब्ध कराएं।", "ದಯವಿಟ್ಟು ಹ್ಯಾಂಡ್ ಸ್ಯಾನಿಟೈಸರ್ ಮತ್ತು ಸಾಬೂನು ನೀಡಿ.", "Low", "HAND + SANITIZER + SOAP + GIVE"),
        ("I need a fresh dental toothbrush and paste.", "मुझे एक नया टूथब्रश और टूथपेस्ट चाहिए।", "ನನಗೆ ಹೊಸ ಟೂತ್ ಬ್ರಷ್ ಮತ್ತು ಪೇಸ್ಟ್ ಬೇಕು.", "Low", "TOOTHBRUSH + PASTE + FRESH + NEED"),
        ("The bathroom floor is slippery, please clean it.", "शौचालय का फर्श गीला और फिसलन भरा है, साफ करें।", "ಸ್ನಾನಗೃಹದ ನೆಲ ಜಾರುತ್ತಿದೆ, ದಯವಿಟ್ಟು ಸ್ವಚ್ಛಗೊಳಿಸಿ.", "Low", "RESTROOM + FLOOR + SLIPPERY + CLEAN"),
        ("I need clean paper tissues or wet wipes.", "मुझे साफ टिशू पेपर या वेट वाइಪ್ಸ್ चाहिए।", "ನನಗೆ ಶುಚಿಯಾದ ಟಿಶ್ಯೂ ಪೇಪರ್ ಅಥವಾ ವೆಟ್ ವೈಪ್ಸ್ ಬೇಕು.", "Low", "TISSUES + WIPES + CLEAN + NEED"),
        ("Please empty the bedside urinary catheter bag.", "कृपया कैथेटर बैग को खाली करें।", "ದಯವಿಟ್ಟು ಕ್ಯಾಥೆಟರ್ ಚೀಲವನ್ನು ಖಾಲಿ ಮಾಡಿ.", "Medium", "CATHETER + BAG + EMPTY + PLEASE"),
        ("Can I wash my hands and face right now?", "क्या मैं अभी अपने हाथ और चेहरा धो सकता हूँ?", "ನಾನು ಈಗ ನನ್ನ ಕೈ ಮತ್ತು ಮುಖವನ್ನು ತೊಳೆಯಬಹುದೇ?", "Low", "HANDS + FACE + WASH + NOW")
    ],
    "discharge_admin": [
        ("When will the doctor approve my hospital discharge?", "डॉक्टर मुझे अस्पताल से कब छुट्टी (डिस्चार्ज) देंगे?", "ವೈದ್ಯರು ನನ್ನನ್ನು ಆಸ್ಪತ್ರೆಯಿಂದ ಯಾವಾಗ ಬಿಡುಗಡೆ ಮಾಡುತ್ತಾರೆ?", "Low", "DOCTOR + DISCHARGE + WHEN + APPROVE?"),
        ("Where is the medical billing and insurance counter?", "मेडिकल बिलिंग और बीमा काउंटर कहाँ है?", "ಮೆಡಿಕಲ್ ಬಿಲ್ಲಿಂಗ್ ಮತ್ತು ವಿಮಾ ಕೌಂಟರ್ ಎಲ್ಲಿದೆ?", "Low", "BILLING + INSURANCE + COUNTER + WHERE?"),
        ("Has the cashless insurance claim been approved?", "क्या कैशलेस स्वास्थ्य बीमा दावा स्वीकृत हो गया है?", "ನಗದು ರಹಿತ ಆರೋಗ್ಯ ವಿಮೆ ಕ್ಲೈಮ್ ಅನುಮೋದನೆಗೊಂಡಿದೆಯೇ?", "Low", "CASHLESS + INSURANCE + CLAIM + APPROVED?"),
        ("Please give me the final discharge summary papers.", "कृपया मुझे अंतिम डिस्चार्ज सारांश पत्र दें।", "ದಯವಿಟ್ಟು ನನಗೆ ಅಂತಿಮ ಡಿಸ್ಚಾರ್ಜ್ ಸಾರಾಂಶ ಪತ್ರಗಳನ್ನು ನೀಡಿ.", "Low", "DISCHARGE + SUMMARY + PAPERS + GIVE"),
        ("When should I come back for the follow-up visit?", "मुझे फॉलो-अप चेकअप के लिए दोबारा कब आना है?", "ನಾನು ತಪಾಸಣೆಗೆ ಮತ್ತೆ ಯಾವಾಗ ಬರಬೇಕು?", "Low", "FOLLOW-UP + VISIT + WHEN + COME?"),
        ("Can you call my family attendant inside?", "क्या आप मेरे परिवार के सदस्य को अंदर बुला सकते हैं?", "ನನ್ನ ಕುಟುಂಬದ ಸದಸ್ಯರನ್ನು ಒಳಗೆ ಕರೆಯಬಹುದೇ?", "Low", "FAMILY + ATTENDANT + INSIDE + CALL"),
        ("I need an official medical certificate for work.", "मुझे काम के लिए एक आधिकारिक मेडिकल प्रमाणपत्र चाहिए।", "ನನಗೆ ಕೆಲಸದ ರಜೆಗಾಗಿ ವೈದ್ಯಕೀಯ ಪ್ರಮಾಣಪತ್ರ ಬೇಕು.", "Low", "MEDICAL + CERTIFICATE + NEED"),
        ("Where can I collect my post-discharge medications?", "डिस्चार्ज के बाद की दवाएं मुझे कहाँ से मिलेंगी?", "ಡಿಸ್ಚಾರ್ಜ್ ನಂತರದ ಔಷಧಿಗಳನ್ನು ನಾನು ಎಲ್ಲಿ ಪಡೆಯಬಹುದು?", "Low", "DISCHARGE + MEDICATIONS + PHARMACY + WHERE?"),
        ("Can I get an itemized hospital bill breakdown?", "क्या मुझे अस्पताल बिल का विस्तृत विवरण मिल सकता है?", "ನನಗೆ ಆಸ್ಪತ್ರೆಯ ಬಿಲ್ ವಿವರಣಾ ಪಟ್ಟಿ ಸಿಗಬಹುದೇ?", "Low", "HOSPITAL + BILL + ITEMIZED + NEED"),
        ("Is transportation or ambulance arranged for home?", "क्या घर जाने के लिए वाहन या एम्बुलेंस की व्यवस्था है?", "ಮನೆಗೆ ಹೋಗಲು ವಾಹನ ಅಥವಾ ಆಂಬ್ಯುಲೆನ್ಸ್ ವ್ಯವಸ್ಥೆ ಇದೆಯೇ?", "Low", "HOME + TRANSPORT + AMBULANCE + ARRANGED?")
    ],
    "pediatric_maternal": [
        ("The baby is crying continuously and will not feed.", "बच्चा लगातार रो रहा है और दूध नहीं पी रहा है।", "ಮಗು ನಿರಂತರವಾಗಿ ಅಳುತ್ತಿದೆ ಮತ್ತು ಹಾಲು ಕುಡಿಯುತ್ತಿಲ್ಲ.", "Medium", "BABY + CRYING + FEED + NOT"),
        ("When is the baby's next vaccination dose due?", "बच्चे का अगला टीकाकरण कब होना है?", "ಮಗುವಿನ ಮುಂದಿನ ಲಸಿಕೆ ಯಾವಾಗ ನೀಡಬೇಕು?", "Low", "BABY + VACCINE + NEXT + WHEN?"),
        ("I am experiencing labor contractions.", "मुझे प्रसव पीड़ा संकुचन शुरू हो गए हैं।", "ನನಗೆ ಹೆರಿಗೆ ನೋವಿನ ಸೆಳೆತ ಪ್ರಾರಂಭವಾಗಿದೆ.", "High", "LABOR + CONTRACTION + PAIN + START"),
        ("Can the pediatrician examine my child?", "क्या बाल रोग विशेषज्ञ मेरे बच्चे की जांच कर सकते हैं?", "ಮಕ್ಕಳ ತಜ್ಞರು ನನ್ನ ಮಗುವನ್ನು ಪರೀಕ್ಷಿಸಬಹುದೇ?", "Medium", "PEDIATRICIAN + CHILD + EXAMINE + CAN?"),
        ("I need a breast pump or feeding bottle.", "मुझे ब्रेस्ट पंप या फीडिंग बोतल चाहिए।", "ನನಗೆ ಬ್ರೆಸ್ಟ್ ಪಂಪ್ ಅಥವಾ ಫೀಡಿಂಗ್ ಬಾಟಲ್ ಬೇಕು.", "Low", "BREAST-PUMP + BOTTLE + NEED"),
        ("The child has developed red skin rashes.", "बच्चे के शरीर पर लाल चकत्ते पड़ गए हैं।", "ಮಗುವಿನ ಮೈಮೇಲೆ ಕೆಂಪು ದದ್ದುಗಳು ಬಂದಿವೆ.", "Medium", "CHILD + SKIN + RED + RASHES"),
        ("Please weigh the newborn baby today.", "कृपया आज नवजात शिशु का वजन करें।", "ದಯವಿಟ್ಟು ನವಜಾತ ಶಿಶುವಿನ ತೂಕವನ್ನು ಇಂದು ಪರೀಕ್ಷಿಸಿ.", "Low", "NEWBORN + BABY + WEIGHT + MEASURE"),
        ("The child's fever has not reduced after syrup.", "सिरप देने के बाद भी बच्चे का बुखार नहीं उतरा।", "ಸಿರಪ್ ನೀಡಿದ ನಂತರವೂ ಮಗುವಿನ ಜ್ವರ ಇಳಿದಿಲ್ಲ.", "Medium", "CHILD + FEVER + SYRUP + NOT + REDUCE"),
        ("Where is the neonatal nursery ward located?", "नवजात शिशु नर्सरी वार्ड कहाँ स्थित है?", "ನವಜಾತ ಶಿಶುಗಳ ನರ್ಸರಿ ವಾರ್ಡ್ ಎಲ್ಲಿದೆ?", "Low", "NEONATAL + NURSERY + WARD + WHERE?"),
        ("Can the mother have warm water and nutritious broth?", "क्या माँ को गुनगुना पानी और पौष्टिक सूप मिल सकता है?", "ತಾಯಿಗೆ ಬೆಚ್ಚಗಿನ ನೀರು ಮತ್ತು ಪೌಷ್ಟಿಕ ಸೂಪ್ ಸಿಗಬಹುದೇ?", "Low", "MOTHER + WARM + WATER + BROTH + WANT")
    ]
}

phrase_list = []
phrase_id = 1
for cat, items in hospital_categories.items():
    for en, hi, kn, urgency, sign_seq in items:
        phrase_list.append({
            "id": phrase_id,
            "category": cat,
            "english": en,
            "hindi": hi,
            "kannada": kn,
            "urgency": urgency,
            "sign_sequence": sign_seq,
            "keywords": [w.lower().strip(".,!?") for w in en.split()]
        })
        phrase_id += 1

with open("hospital_phrases.json", "w", encoding="utf-8") as f:
    json.dump({
        "total_phrases": len(phrase_list),
        "total_categories": len(hospital_categories),
        "categories": list(hospital_categories.keys()),
        "phrases": phrase_list
    }, f, indent=2, ensure_ascii=False)

print(f"Generated hospital_phrases.json with {len(phrase_list)} phrases across {len(hospital_categories)} categories.")

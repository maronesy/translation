# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 506 (printed ٥٠٥)."""

PAGE_NUMBER = 506
PRINTED_PAGE = "٥٠٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(بحذف حرف المضارعة) احتراز» at the foot of PDF p. 505 (mid-sentence).
    {"type": "matn",
     "ar": "عن مثل قوله تعالى: ﴿فبذلك فليفرحوا﴾[[١]] فيمن قرأ على صيغة الخطاب، وعن مثل: «صه ورويد».",
     "en": "…from such as His words, the Exalted, “So in that let them rejoice” (Qurʾān, Sūrat Yūnus 10:58), in the reading of those who read it in the second-person form, and from such as “ṣah” (hush) and “ruwayda” (gently)."},
    {"type": "matn",
     "ar": "(وحكم آخره) أي: آخر الأمر في الحقيقة عند البصريين الوقف والبناء على السكون،",
     "en": "(And the rule for its end), that is, the end of the imperative, is in reality, according to the Baṣrans, the pause and indeclinability on sukūn,"},
    {"type": "matn",
     "ar": "لانتفاء ما يقتضي إعرابه، وهو حرف المضارعة؛ لأن مشابهته للاسم المقتضية للإعراب إنما هي بسببه،",
     "en": "because what would require its inflection is absent, namely the prefix of the muḍāriʿ; for its resemblance to the noun, which requires inflection, is only by reason of it;"},
    {"type": "matn",
     "ar": "وفي الصورة (حكم المجزوم) أي: مثل حكم المضارع المجزوم في إسكان الصحيح وسقوط نون الإعراب وحرف العلة؛",
     "en": "and in outward form it is (the rule of the jussive), that is, like the rule of the jussive muḍāriʿ, in making the sound [final letter] quiescent and in dropping the nūn of inflection and the weak letter;"},
    {"type": "matn",
     "ar": "لأنه لما شابه ما فيه اللام من المجزوم معنى، أعطي له حكمه",
     "en": "because, since it resembles in meaning the jussive that has the lām [of command], it was given its rule."},
    {"type": "matn",
     "ar": "تقول: «اضرب، اضربا، اضربوا، واخش، واغز، وارم» كما تقول: «لم يضرب، لم يضربا، ولم يضربوا، ولم يخش، ولم يغز، ولم يرم»،",
     "en": "You say “iḍrib, iḍribā, iḍribū, wa-khsha, wa-ghzu, wa-rmi” (strike [sg., du., pl.], fear, raid, throw), just as you say “lam yaḍrib, lam yaḍribā, wa-lam yaḍribū, wa-lam yakhsha, wa-lam yaghzu, wa-lam yarmi”."},
    {"type": "matn",
     "ar": "وذهب الكوفيون إلى أنه معرب مجزوم بلام مقدرة.",
     "en": "The Kūfans held that it is inflected, put in the jussive by a supposed lām."},
    {"type": "matn",
     "ar": "(فإن كان بعده) أي: بعد حرف المضارعة أو بعد حذفه متحرك، أسكن آخره وجعل ما بقي أمرا،",
     "en": "(So if after it), that is, after the prefix of the muḍāriʿ, or after its omission, there is a voweled letter, its end is made quiescent and what remains is made the imperative:"},
    {"type": "matn",
     "ar": "تقول في «تعد»: عد، وفي «تضارب»: ضارب، ولم يذكر المصنف هذا القسم لظهوره.",
     "en": "you say for “taʿidu”: ʿid, and for “tuḍāribu”: ḍārib. The author did not mention this division because it is evident."},
    {"type": "matn",
     "ar": "وإن كان بعده حرف (ساكن وليس) المضارع (برباعي) والمراد بالرباعي ههنا: «ما يكون ماضيه على أربعة أحرف من المزيد فيه[[٢]]»، وإنما هو باب الإفعال لا غير",
     "en": "And if after it there is a (quiescent) letter, (and) the muḍāriʿ (is not quadriliteral) — what is meant by quadriliteral here is “that whose past consists of four letters, of the augmented [verbs]”, which is only the form ifʿāl and no other —"},
    {"type": "matn",
     "ar": "(زدت همزة وصل) على ما بقي بعد حذف حرف المضارعة؛ ليتوصل بها إلى النطق بالساكن",
     "en": "(you add a connecting hamza (hamzat waṣl)) to what remains after omitting the prefix of the muḍāriʿ, so that by it one may reach the pronunciation of the quiescent letter,"},
    {"type": "matn",
     "ar": "حال كون تلك الهمزة[[٣]] (مضمومة إن كان[[٤]] بعده) أي: بعد الساكن (ضمة)",
     "en": "that hamza being (with ḍamma if there is after it), that is, after the quiescent letter, (a ḍamma),"},
    {"type": "matn",
     "ar": "دفعا للالتباس بالمضارع المتكلم المعلوم على تقدير الفتح، وتحرزا عن الخروج من الكسرة إلى الضمة على تقدير الكسرة،",
     "en": "to avoid confusion with the first-person active muḍāriʿ on the supposition of a fatḥa, and to guard against passing from a kasra to a ḍamma on the supposition of a kasra;"},
    # REVIEW: the clause «فإنه إذا قيل في: «أقتل» بكسر التاء» has no apodosis as printed; transcribed as printed.
    {"type": "matn",
     "ar": "فإنه إذا قيل في: «أقتل» بكسر التاء",
     "en": "for if it were said for “uqtul” with a kasra on the tāʾ…"},
    # REVIEW: printed «بعده ضمه» (final hāʾ, apparently for «ضمة»); transcribed as printed.
    {"type": "matn",
     "ar": "(ومكسورة فيما سواه) أي: فيما سوى ساكن بعده ضمه سواء كان بعده كسرة أو فتحة،",
     "en": "(And with kasra in what is other than that), that is, in what is other than a quiescent letter followed by a ḍamma, whether a kasra or a fatḥa follows it;"},
    {"type": "matn",
     "ar": "فإنه لو ضم في مثل: «أضرب» التبس بالماضي المجهول من الإضراب، ولو فتح لالتبس بالأمر منه،",
     "en": "for if it were given a ḍamma in such as “iḍrib”, it would be confused with the passive past of iḍrāb (uḍriba), and if given a fatḥa it would be confused with its imperative (aḍrib);"},
    {"type": "matn",
     "ar": "ولو ضم في «أعلم» لالتبس بالمضارع المجهول المتكلم، ولو فتح لالتبس بالماضي الرباعي",
     "en": "and if given a ḍamma in “iʿlam” it would be confused with the first-person passive muḍāriʿ (uʿlamu), and if given a fatḥa, with the quadriliteral past (aʿlama)."},
    {"type": "matn",
     "ar": "(نحو: «اقتل») مثال لما يكون بعد الساكن ضمة (و«اضرب») مثال",
     "en": "(As in “uqtul”): an example of what has a ḍamma after the quiescent letter; (and “iḍrib”): an example…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "سورة يونس: ٥٨.",
     "en": "Qurʾān, Sūrat Yūnus 10:58."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "زائد لا طائل تحته؛ إذ الرباعي المجرد خرج بقوله: إن كان بعده ساكن.",
     "en": "Superfluous and of no use, since the unaugmented quadriliteral is already excluded by his words “if there is a quiescent letter after it”."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "اختار الحال؛ لأن اللازم ضم الهمزة وقت الزيادة، وفي الصفة يتبادر سبق ضمها على الزيادة على ما مر في تعريف الكلمة،",
     "en": "He chose the circumstantial (ḥāl) because what is required is that the hamza take the ḍamma at the time of the addition, whereas with an attribute what first comes to mind is that its ḍamma precedes the addition, as was discussed under the definition of the word (kalima);"},
    {"type": "pair",
     "ar": "وجاز تأخير الحال لكون صاحبها نكرة مخصوصة بالإضافة.",
     "en": "and placing the ḥāl after [its head] is permitted because its head is an indefinite noun specified by annexation."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "شرط يدل على جوابه ما قبله.",
     "en": "A condition whose apodosis is indicated by what precedes it."},
]

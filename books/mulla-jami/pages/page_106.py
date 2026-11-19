# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 106 (printed ١٠٥)."""

PAGE_NUMBER = 106
PRINTED_PAGE = "١٠٥"   # Arabic-Indic, as printed

BLOCKS = [
    {"type": "matn",
     "ar": "وإنما جعلت شرطا[[١]] لئلا يتصرف فيها[[٢]] مثل تصرفاتهم في كلامهم[[٣]]، فيضعف فيه العجمة، فلا تصلح سببا لمنع الصرف.",
     "en": "It [proper-nounhood] was made a condition only lest [the foreign word] be handled the way [the Arabs] handle [words] in their speech, whereby its foreignness would be weakened in it and so would not be fit to be a cause for triptote-prevention."},
    {"type": "matn",
     "ar": "فعلى هذا لو سمي بمثل «لجام» لا يمتنع صرفه، لعدم علميته في العجمية.",
     "en": "Accordingly, were something named with the likes of “lijām,” its full inflection would not be prevented, because it was not a proper name in the non-Arab tongue."},
    {"type": "matn",
     "ar": "٢-(و) شرطها الثاني: أحد الأمرين: (تحرك) الحرف (الأوسط[[٤]] أو زيادة على الثلاثة) أي: على ثلاثة أحرف، لئلا تعارض الخفة أحد السببين.",
     "en": "2 — Its second condition [is] one of two things: that the middle letter be vowelled, or that [the word] exceed three [letters] — that is, exceed three consonants — so that lightness (khiffa) may not counteract one of the two causes."},
    {"type": "matn",
     "ar": "(فنوح منصرف) هذا تفريع بالنظر إلى الشرط الثاني، فانصراف «نوح» إنما هو لانتفاء الشرط الثاني.",
     "en": "(“So Nūḥ is a triptote”) — this is a corollary with respect to the second condition; the full inflection of “Nūḥ” is only because the second condition is absent."},
    {"type": "matn",
     "ar": "وهذا اختيار المصنف[[٥]]؛ لأن العجمة سبب ضعيف؛ لأنه أمر معنوي[[٦]]، فلا يجوز اعتبارها مع سكون الأوسط.",
     "en": "This is the author’s preference, because foreignness is a weak cause, being an abstract [non-phonetic] matter; so it may not be reckoned along with the quiescence of the middle letter."},
    {"type": "matn",
     "ar": "وأما التأنيث المعنوي: فإن له علامة مقدرة تظهر في بعض التصرفات، فله نوع قوة، فجاز أن يعتبر مع سكون الأوسط، وألا يعتبر.",
     "en": "As for abstract [semantic] feminization: it has an implied marker that becomes manifest in some inflectional operations, so it possesses a kind of strength; hence it may be reckoned along with the quiescence of the middle letter, and it may equally not be reckoned."},

    {"type": "rule"},

    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "يحقق الاشتراك ما قاله الشيخ الرضي. وهو: أن العجمة في الأعجمي يقتضي ألا يتصرف فيها كلام العرب، ووقوعها في كلامهم يقتضي أن يتصرف فيها تصرف كلامهم.",
     "en": "The sharing [between the two considerations] is confirmed by what al-Shaykh al-Raḍī said, namely: that foreignness in a foreign word requires that Arab usage not operate upon it, while its occurring in their speech requires that their usage operate upon it as it operates upon [their own words]."},
    {"type": "pair",
     "ar": "فإذا وقعت فيه أولا مع العلمية، وهي منافية للام والإضافة، فامتنعتا معها جاز أن يمتنع معها ما يعاقبهما أيضا، أعني التنوين رعاية لحق العجمة حين أمكنت،",
     "en": "So when it first occurs in [Arabic usage] together with proper-nounhood — which is incompatible with the article and with annexation — and both of these are precluded by it, then it becomes admissible that what alternates with them, namely nunation (tanwīn), be likewise precluded along with it, in observance of the right of foreignness whenever that is possible;"},
    {"type": "pair",
     "ar": "فيتبع الكسر التنوين على ما هو عادة، وبقي الاسم قابلا لسائر تصرفات كلامهم على ما يقتضيه وقوعه فيه لما تقرر أن الطارئ يزيل حكم المطرو عليه،",
     "en": "so nunation follows the kasra, as is customary, while the noun remains susceptible to the rest of their usage’s operations as its occurring in [their speech] requires — in accordance with the established principle that a supervening [state] removes the ruling of that which it supervenes upon;"},
    {"type": "pair",
     "ar": "فيقبل الإعراب وياء النسبة، وتخفيف ما يستثقل فيه بحذف بعض الحروف وقلب بعضها، نحو: جرجان وآذربايجان في كركان وآذر بايكان.",
     "en": "so it admits inflection, the yāʾ of relation, and the lightening of what is felt heavy in it by dropping some letters and altering others — as in “Jurjān” and “Ādharbāyjān” for “Kurkān” and “Ādhar Bāykān.”"},
    {"type": "pair",
     "ar": "وأما إذا لم يقع الأعجمي في كلام العرب أولا مع العلمية قبل اللام والإضافة؛ إذ لا مانع، فيقبل التنوين أيضا مع الكسر، كما يقبل سائر التصرفات.",
     "en": "But if the foreign word does not first enter Arab usage together with proper-nounhood before the article and annexation — since there is then no impediment — it admits nunation too along with the kasra, just as it admits the rest of the operations."},

    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: في الكلمة العجمية مثل تصرفاتهم في كلامهم، فيمتنع عن الإضافة واللام، وما يقابلهما أي: التنوين، فلا تدخله الكسرة أيضا.",
     "en": "That is: [that Arab usage not operate] upon the foreign word the way it operates in their speech, so that it is barred from annexation and the article, and from what corresponds to them — namely nunation — so that the kasra too does not enter it."},
    {"type": "pair",
     "ar": "وإن لم يمتنع من قبول ياء النسبة والإعراب وقلب بعض الحروف وحذفه تخفيفا، نحو: جرجان في كركان، وجبرال وجبريل في جبرائيل.",
     "en": "though it is not barred from admitting the yāʾ of relation, inflection, and the altering of some letters and their dropping for lightening — as in “Jurjān” for “Kurkān,” and “Jibrāl” and “Jibrīl” for “Jibrāʾīl.”"},

    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: في كلام العرب كإدخال اللام والإضافة. ثم إذا لم يتصرف فيه بإدخالهما ناسب ألا يتصرف فيه بإدخال التنوين أيضا؛ لأنها من مقولة واحدة في الكون لإتمام الكلمة.",
     "en": "That is: within Arab usage, such as prefixing the article and [applying] annexation. Then, if it is not operated upon by introducing those two, it is fitting that it likewise not be operated upon by introducing nunation, since they all belong to one category in existence [i.e., serving] to complete the word."},

    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "ذهب سيبويه وأكثر النحاة إلى أن الشرط الثاني الزيادة على الثلاثة، ولا اعتبار لتحرك الأوسط في تأثير العجمة؛",
     "en": "Sībawayh and most grammarians held that the second condition is exceeding three [letters], and that the vowelling of the middle letter is of no account in the effectiveness of foreignness;"},
    {"type": "pair",
     "ar": "لأن الثلاثي -سواء كان متحرك الأوسط أو ساكنه- خفيف، ووضع كلام العجم على الطول، فكأن الثلاثي ليس منه.",
     "en": "because the triliteral — whether its middle letter is vowelled or quiescent — is light, whereas non-Arab speech was coined upon length; so it is as though the triliteral is not [reckoned] among it."},

    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وذهب الزمخشري إلى أن «نوحا» كهند. ولعله قاس العجمة على التأنيث المعنوي، أو حمله على ذلك تحتم منع الصرف [في] ماه وجور.",
     "en": "Al-Zamakhsharī held that “Nūḥ” is like “Hind.” Perhaps he drew an analogy between foreignness and abstract feminization, or he was led to that by the [seeming] necessity of preventing full inflection in “Māh” and “Jūr.”"},

    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: ليس له علامة لفظية. الضمير للعجمة، وسبب تذكيره أمر معنوي، وضمير اعتبارها للعجمة أيضا.",
     "en": "That is: it has no phonetic marker. The pronoun [in “being an abstract matter”] refers to foreignness, and the reason for its masculine form is [that its predicate is] “an abstract matter”; the pronoun in “reckoning it” also refers to foreignness."},
]

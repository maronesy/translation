# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 364 (printed ٣٦٣)."""

PAGE_NUMBER = 364
PRINTED_PAGE = "٣٦٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Follows «فمتى أمكن الاتصال لا يسوغ الانفصال.» at the foot of PDF p. 363 (new sentence).
    {"type": "matn",
     "ar": "(وذلك) أي: تعذر المتصل (بالتقديم[[١]])، أي: تقديم الضمير (على عامله)؛ لأنه إذا تقدم على عامله لا يمكن أن يتصل به؛ إذ الاتصال إنما يكون بآخر العامل[[٢]].",
     "en": "(That is) — that is, the connected [pronoun] becomes impossible — (through fronting), that is, fronting the pronoun (before its governor); for if it comes before its governor it cannot be joined to it, since joining occurs only at the end of the governor."},
    {"type": "matn",
     "ar": "(أو بالفصل[[٣]]) الواقع (لغرض[[٤]]) لا يحصل إلا به؛ إذ الفصل ينافي الاتصال، وبتركه يفوت الغرض.",
     "en": "(Or through separation) that occurs (for a purpose) which is attained only by it; for separation is incompatible with connection, and by abandoning it the purpose would be lost."},
    {"type": "matn",
     "ar": "(أو بالحذف) أي: حذف عامله[[٥]]؛ لأنه إذا حذف عامله لا يوجد ما يتصل به.",
     "en": "(Or through elision), that is, elision of its governor; for if its governor is elided, there is nothing to which it could be joined."},
    {"type": "matn",
     "ar": "(أو بكون العامل) أي: عامله (معنويا) لامتناع اتصال اللفظ بالمعنى.",
     "en": "(Or through the governor), that is, its governor, (being abstract) (maʿnawī), since a word cannot be joined to a meaning."},
    {"type": "matn",
     "ar": "(أو) بكون عامله (حرفا، والضمير) المعمول له (مرفوع[[٦]])؛ إذ الضمير المرفوع لا يتصل بالحرف؛ لأنه خلاف لغتهم، بخلاف المنصوب نحو: «إنني وإنك».",
     "en": "(Or) through its governor being (a particle while the pronoun) governed by it (is in the nominative); for a nominative pronoun is not joined to a particle, since that runs contrary to their usage, unlike the accusative, as in “innanī” and “innaka”."},
    {"type": "matn",
     "ar": "(أو بكونه) أي: بكون الضمير (مسندا إليه) أي: إلى ذلك الضمير (صفة جرت[[٧]]",
     "en": "(Or through its), that is, the pronoun’s, (having predicated of it), that is, of that pronoun, (an adjective that is applied…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "قيل: تفصيله قاصر؛ لأنه لم يشمل «أقائم أنتم» وفاعل المصدر",
     "en": "It has been said: his breakdown is deficient, because it does not include “a-qāʾimun antum” (are you standing?) or the agent of the verbal noun."},
    {"type": "pair",
     "ar": "أقول: أقائم أنتم داخل في الفصل لغرض، وهو رفع الالتباس؛ إذ لو استتر لم يعلم أنه المخاطب أو الغائب أو المتكلم،",
     "en": "I say: “a-qāʾimun antum” falls under separation for a purpose, namely removing ambiguity; for if [the pronoun] were concealed, it would not be known whether it is the addressee, the absent or the speaker."},
    {"type": "pair",
     "ar": "ومنه فصل المفعول الثاني إذا التبس بالمفعول الأول بالاتصال.",
     "en": "Of this kind is the separation of the second object when, by being connected, it would be confused with the first object."},
    {"type": "pair",
     "ar": "وأما إذا لم يلتبس، فالاتصال في باب «أعطيت»، والانفصال في باب «علمت» أولى،",
     "en": "When it is not confused, however, connection is preferable in the category of “aʿṭaytu” (I gave), and separation in the category of “ʿalimtu” (I knew)."},
    {"type": "pair",
     "ar": "ومنه فصل الضمير بعد «إنما»، فإنه يجب عند الالتباس وعند عدم الالتباس لا يجب، شهد به شرح المفتاح،",
     "en": "Of this kind too is the separation of the pronoun after “innamā”: it is obligatory when there is ambiguity and not obligatory when there is none, as the commentary on al-Miftāḥ attests."},
    {"type": "pair",
     "ar": "وإنما يتم الثاني لو وجد فاعل المصدر الضمير غير مضاف إليه المصدر.",
     "en": "The second [objection] would hold only if there were found a pronominal agent of a verbal noun to which the verbal noun is not annexed."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لأن الضمير المتصل كالجزء الأخير من عامله، فإذا لم يكن قبله عامل، بل كان مؤخرا أو محذوفا، فكيف يكون كالجزء الأخير.",
     "en": "Because the connected pronoun is like the last part of its governor; so if there is no governor before it, the governor being placed after it or elided, how could it be like the last part?"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "من بابه ما وقع تابعا تأكيدا أو بدلا أو عطفا.",
     "en": "Belonging to this category is what occurs as a follower (tābiʿ): as an emphasis (taʾkīd), a substitute (badal) or a conjunct (ʿaṭf)."},
    {"type": "pair",
     "ar": "وكذا ما وقع بعد \"إما\" المفيدة للشك في أول الأمر، نحو: جاءني إما أنت أو زيد،",
     "en": "Likewise what occurs after “immā” that conveys doubt from the outset, as in “jāʾanī immā anta aw Zaydun” (either you or Zayd came to me);"},
    {"type": "pair",
     "ar": "وما وقع ثاني باب «علمت وأعطيت» إذا كان اتصال يورث التباسا بالمفعول الأول.",
     "en": "and what occurs as the second [object] in the category of “ʿalimtu” and “aʿṭaytu” when connection would cause confusion with the first object."},
    {"type": "pair",
     "ar": "أما إذا لم يلتبس، فالاتصال في باب «أعطيت» أولى، والانفصال في باب «علمت» أولى.",
     "en": "When there is no confusion, connection is preferable in the category of “aʿṭaytu”, and separation is preferable in the category of “ʿalimtu”."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: احترز به عن نحو: «ضرب زيد إياك»، فإنه لا يجوز ذلك المثال مع الفصل؛ إذ لا غرض فيه؛ لأن قولك: «ضربك زيد» بمعناه،",
     "en": "Shaykh al-Raḍī said: by this he excludes such as “ḍaraba Zaydun iyyāka” (Zayd struck you), for that example is not permitted with separation, since there is no purpose in it, your saying “ḍarabaka Zaydun” having the same meaning."},
    {"type": "pair",
     "ar": "ثم اعترض عليه بأن التقديم يفيد الاهتمام.",
     "en": "Then it was objected against him that fronting conveys emphasis of concern (ihtimām)."},
    {"type": "pair",
     "ar": "فأجاب الرضي: بأن تقديم المفعول لا يفيد ذلك، بل قد يكون ذلك لاتساع الكلام،",
     "en": "Al-Raḍī answered that fronting the object does not convey that; rather, it may occur merely for latitude of expression (ittisāʿ al-kalām)."},
    {"type": "pair",
     "ar": "بل قيل: إن تقديم المفعول على الفعل يفيد كونه أهم.",
     "en": "Rather, it has been said that fronting the object before the verb conveys that it is of greater concern."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "ينبغي أن يراد حذف عامله دونه؛ إذ لو حذفا معا لم يخرج من الاتصال كقولك: «زيدا ضربته»،",
     "en": "What should be meant is elision of its governor without [the pronoun]; for if both were elided together, it would not depart from connection, as in your saying “Zaydan ḍarabtuhu” (Zayd, I struck him),"},
    {"type": "pair",
     "ar": "فإنه في تقدير «ضربت زيدا» فلم يخرج الضمير بحذف عامله عن الاتصال.",
     "en": "for it is in the implied form “ḍarabtu Zaydan” (I struck Zayd), and the pronoun did not depart from connection through the elision of its governor."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لا يقال: الأولى غير مجرور أو منصوب لئلا ينتقض بضمير «أنه»، فإنه مرفوع المحل كما أنه منصوب المحل؛",
     "en": "It should not be said: it would be better [to say] “not genitive or accusative”, so that it is not broken by the pronoun of “annahu”, which is nominative in position just as it is accusative in position;"},
    {"type": "pair",
     "ar": "لأنا نقول: المراد بالمرفوع ما هو ضمير مرفوع في اصطلاح باب المضمرات.",
     "en": "for we say: what is meant by “nominative” is what is a nominative pronoun in the terminology of the chapter on pronouns."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "المراد بالجريان أن يكون نعتا أو حالا أو صلة أو خبرا.",
     "en": "What is meant by “being applied” (jarayān) is its being a qualifier (naʿt), a circumstantial (ḥāl), a relative clause (ṣila) or a predicate (khabar)."},
    {"type": "pair",
     "ar": "ولو قال: أو بكونه صفة لم تجر على من هي له لكان أشمل لدخول «أقائم أنتم» فيه.",
     "en": "Had he said “or through its being an adjective not applied to the one to whom it belongs”, it would have been more comprehensive, since “a-qāʾimun antum” would fall under it."},
    {"type": "pair",
     "ar": "فإن قلت: لا حاجة إلى قوله: أو بكونه صفة جرت على غير من هي له بعد قوله: أو بالفصل لغرض؛ لأن الفصل فيه لرفع الالتباس؟",
     "en": "If you say: there is no need for his words “or through its being an adjective applied to other than the one to whom it belongs” after his words “or through separation for a purpose”, since the separation in it is for removing ambiguity?"},
    {"type": "pair",
     "ar": "قلت: يجب الفصل فيما لا يلتبس أيضا. وبهذا ظهر وجه قوي لاختيار التمثيل بما لا يلتبس فيه.",
     "en": "I say: separation is obligatory also where there is no ambiguity. By this a strong reason appears for choosing to illustrate with a case in which there is no ambiguity."},
    {"type": "pair",
     "ar": "وإنما قال: صفة لأن الفعل الجاري على غير من هو له لا يجب فيه الضمير المنفصل بالاتفاق على ما في الرضي.",
     "en": "He said “an adjective” only because, in a verb applied to other than the one to whom it belongs, the separate pronoun is not obligatory, by agreement, according to what is in al-Raḍī."},
]

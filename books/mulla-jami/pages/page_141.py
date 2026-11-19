# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 141 (printed ١٤٠)."""

PAGE_NUMBER = 141
PRINTED_PAGE = "١٤٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base/commentary text (matn) ----------------
    {"type": "matn",
     "ar": "«نعم» في مقامها[[١]]، وهذا الحذف جائز بقرينة السؤال لا واجب[[٢]]؛",
     "en": "“Yes” (naʿam) stands in its place; and this ellipsis is permissible by virtue of the indication of the question, not obligatory;"},
    {"type": "matn",
     "ar": "لعدم قيام ما يؤدي مؤداه في مقامه كالمفسر، فيلزم في الكلام استدراك،",
     "en": "because there is nothing that fulfills its function standing in its place like an explicator (mufassir), so a [need for] rectification (istidrāk) would arise in the speech;"},
    {"type": "matn",
     "ar": "وإنما قدر الجملة الفعلية لا الاسمية بأن يقال أي: «نعم، زيد قام»؛ ليكون الجواب مطابقا للسؤال في كونه جملة فعلية.",
     "en": "and it is the verbal sentence, not the nominal one, that is estimated—such that one says, that is: “Yes, Zayd stood”—so that the answer conforms to the question in its being a verbal sentence."},

    {"type": "section", "ar": "[ التنازع ]",
     "en": "Government-Conflict (al-Tanāzuʿ)"},

    {"type": "matn",
     "ar": "(وإذا تنازع الفعلان[[٣]]) بل العاملان[[٤]]؛ إذ التنازع يجري في غير الفعل أيضا[[٥]]،",
     "en": "(And when the two verbs contend—wa-idhā tanāzaʿa al-fiʿlān), rather [when] the two governors (al-ʿāmilān) [contend]; for tanāzuʿ occurs in other than the verb as well,"},
    {"type": "matn",
     "ar": "نحو: «زيد معط ومكرم عمرا»، و«بكر كريم وشريف أبوه».",
     "en": "as in: “Zayd is a giver and an honorer of ʿAmr,” and “Bakr is noble, and his father is honorable.”"},
    {"type": "matn",
     "ar": "واقتصر على الفعل[[٦]] لأصالته في العمل.",
     "en": "He restricted [the wording] to the verb because of its being the original [locus] of government (ʿamal)."},
    {"type": "matn",
     "ar": "وإنما قال: «الفعلان» مع أن التنازع قد يقع في أكثر من فعلين[[٧]] اقتصارا على أقل مراتب التنازع، وهو الاثنان",
     "en": "He said “the two verbs”—although tanāzuʿ may occur in more than two verbs—by way of restricting [the statement] to the least degree of tanāzuʿ, which is two;"},
    {"type": "matn",
     "ar": "(ظاهرا) أي: اسما ظاهرا واقعا (بعدهما) أي: بعد الفعلين؛",
     "en": "(an overt [noun]—ẓāhiran), that is: an overt noun occurring (after them both—baʿdahumā), that is: after the two verbs;"},
    {"type": "matn",
     "ar": "إذ المتقدم عليهما والمتوسط بينهما معمول للفعل الأول[[٨]]؛ إذ هو يستحقه قبل الثاني، فلا يكون فيه مجال التنازع،",
     "en": "for what precedes them both and what is placed between them is governed by the first verb; since it merits it before the second, so there is no scope for tanāzuʿ in it;"},
    {"type": "matn",
     "ar": "ومعنى تنازعهما فيه أنهما بحسب",
     "en": "and the meaning of their contending over it is that they, in respect of…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فيه أن كلمة «نعم» إن كانت مذكورة بعد الجملة يكون مذكورة في مقام الجملة بعد حذفها.",
     "en": "In it [there is a difficulty]: that the word “naʿam,” if it is uttered after the sentence, is [only then] uttered in the position of the sentence, after the sentence’s deletion."},
    {"type": "pair",
     "ar": "وأما إذا كانت قبل الجملة فهي مذكورة في مقام نفسها سواء ذكرت الجملة أو حذفت، وههنا ليس كذلك",
     "en": "But if it comes before the sentence, then it is uttered in its own position, whether the sentence is expressed or deleted—and here it is not so;"},
    {"type": "pair",
     "ar": "إلا أن يقال: المراد بذكر «نعم» مقام الجملة الاكتفاء بها عن ذكر الجملة.",
     "en": "unless one says: what is meant by uttering “naʿam” in the position of the sentence is contenting oneself with it in place of uttering the sentence."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "وقد يحذفان وجوبا كما في المنادى، والحال المؤكدة، والتحذير.",
     "en": "The two may be deleted obligatorily, as in the vocative (munādā), the corroborating circumstantial qualifier (al-ḥāl al-muʾakkida), and [the construction of] warning (taḥdhīr)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "من قبيل تجاذبنا الثوب.",
     "en": "[This is] of the sort of “we pulled the garment against one another” (tajādhabnā al-thawb)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "قال بعض المحققين: لكن ينبغي أن يخص العامل بغير المصدرين في نحو: «أعجبني ضرب وقتل زيد»،",
     "en": "Some of the verifying scholars said: yet the governor should be restricted to other than the two verbal nouns (maṣdars), as in: “the striking and the killing of Zayd pleased me,”"},
    {"type": "pair",
     "ar": "فإنه لا يصح فيه قطع النزاع على مذهب البصري والكوفي؛ إذ لا يضمر الفاعل في المصدر.",
     "en": "for the resolution of the contention (qaṭʿ al-nizāʿ) is not valid in it according to the doctrine of the Baṣran and the Kūfan; since the agent is not concealed within the verbal noun."},
    {"type": "pair",
     "ar": "ثم إن الأولى أن يشار إلى أن المراد بالفعل العامل في قوله: وقد يحذف الفعل أيضا.",
     "en": "Then, it would be more fitting to indicate that what is meant by “the verb” is the governor, [as] in his statement: “and the verb, too, may be deleted.”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لكن ينبغي أن يخص العاملان بغير المصدرين، نحو: «أعجبني ضرب وقتل زيد»،",
     "en": "Yet the two governors should be restricted to other than the two verbal nouns, as in: “the striking and the killing of Zayd pleased me,”"},
    {"type": "pair",
     "ar": "فإنه لا يصح فيه قطع التنازع على مذهب البصري والكوفي؛ إذ لا يضمر الفاعل في المصدر،",
     "en": "for the resolution of the tanāzuʿ is not valid in it according to the doctrine of the Baṣran and the Kūfan; since the agent is not concealed within the verbal noun."},
    {"type": "pair",
     "ar": "ولا يذهب عليك أن أولى مقام بالتنبيه على أن المراد بالفعل العامل قوله: والأصل أن يلي الفعل.",
     "en": "And let it not escape you that the place most deserving of an alert that what is meant by “the verb” is the governor is his statement: “and the default is that it [the noun] immediately follows the verb.”"},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "يجوز أن يراد بالفعلين العاملان على طريقة تغليب الأكثر على الأقل، أو الأصل على الفرع.",
     "en": "It is permissible that by “the two verbs” the two governors are intended, by way of giving predominance (taghlīb) to the more frequent over the less frequent, or to the original over the derivative."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "نحو: كما صليت وسلمت وباركت ورحمت وترحمت على إبراهيم.",
     "en": "As in: “as You blessed, granted peace, favored, showed mercy, and had compassion upon Ibrāhīm.”"},
    {"type": "pair",
     "ar": "وحينئذ يكون الأخير كالثاني، والبواقي كالأول عند البصريين.",
     "en": "In that case the last is like the second, and the remaining ones like the first, according to the Baṣrans."},
    {"type": "pair",
     "ar": "والأول هو الأولى، والبواقي كالثاني عند الكوفيين.",
     "en": "And the first is the foremost [governor], and the remaining ones like the second, according to the Kūfans."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "هذا رد لقول بعض الشارحين من أن التنازع متصور في صورة التقديم عليهما إذا كان التنازع في المفعولية،",
     "en": "This is a refutation of the statement of some commentators that tanāzuʿ is conceivable in the case where [the noun] precedes them both, when the tanāzuʿ is over objecthood (mafʿūliyya),"},
    {"type": "pair",
     "ar": "وفي صورة التوسط بينهما أيضا إذا كان التنازع في المفعولية؛ إذ الأول يقتضي الفاعل والثاني المفعول.",
     "en": "and likewise in the case where it is placed between them, when the tanāzuʿ is over objecthood; since the first requires the agent and the second the object."},
    {"type": "pair",
     "ar": "قال عبد الغفور: قوله: «معمول للفعل الأول» اتفاقا.",
     "en": "ʿAbd al-Ghafūr said: his statement “governed by the first verb” [is so] by [scholarly] agreement."},
    {"type": "pair",
     "ar": "فلا يجري فيه النزاع بين الفريقين سواء اعتبر التنازع بين الفعلين كما اعتبر بعضهم أو لم يعتبر.",
     "en": "So the dispute between the two parties does not run in it, whether the tanāzuʿ between the two verbs is taken into account—as some have taken it—or not."},
]
